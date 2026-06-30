
from .models import Group,Split,Expense
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404,redirect

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='registration/signup.html'
    success_url=reverse_lazy('login')

class GroupListView(LoginRequiredMixin,ListView):
    model= Group
    context_object_name='groups'
    template_name='expenses/home.html'

    def get_queryset(self):
        return Group.objects.filter(members=self.request.user)

class GroupCreateView(LoginRequiredMixin,CreateView):
    model=Group
    fields=['name','members']
    template_name='expenses/create_group.html'
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        form.instance.created_by=self.request.user
        return super().form_valid(form)


class GroupDetailView(LoginRequiredMixin,DetailView):
    model=Group
    template_name='expenses/group_detail.html'
    context_object_name= 'group'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['expenses']=Expense.objects.filter(group=self.object)
        balances={}
        members=self.object.members.all()
        for member in members:
            balances[member]=0
        for expense in context['expenses']:
            for split in expense.splits.all():
                if not split.is_paid:
                    balances[split.user]-=split.amount_owed
                    balances[expense.paid_by]+=split.amount_owed

        context['balances']=balances
        return context
                         
class ExpenseCreateView(LoginRequiredMixin,CreateView):
    model=Expense
    template_name='expenses/create_exp.html'
    fields=['title','amount']

    def form_valid(self,form):
        form.instance.paid_by=self.request.user
        form.instance.group=Group.objects.get(pk=self.kwargs['pk'])
        response= super().form_valid(form)
        members=self.object.group.members.all()
        amount_per_person= self.object.amount // members.count()
        for member in members:
            Split.objects.create(
                expense=self.object,
                amount_owed=amount_per_person,
                user=member,
            )
        return response

    def get_success_url(self):
        return reverse_lazy('group_detail',kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['group']=Group.objects.get(pk=self.kwargs['pk'])
        return context
    
class ExpenseDetailView(LoginRequiredMixin,DetailView):
    model= Expense
    template_name="expenses/exp_detail.html"
    context_object_name= 'expense'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['splits']=Split.objects.filter(expense=self.object)
        return context
    
def mark_paid(request,pk):
    split=get_object_or_404(Split,pk=pk)
    split.is_paid=True
    split.save()
    return redirect('expense_detail',pk=split.expense.pk)

class GroupDeleteView(LoginRequiredMixin,DeleteView):
    model= Group
    template_name="expenses/del_group.html"
    success_url=reverse_lazy('home')

class ExpenseDeleteView(LoginRequiredMixin,DeleteView):
    model= Expense
    
    def get_success_url(self):
        return reverse_lazy('group_detail',kwargs={'pk': self.object.group.pk})
    
class GroupUpdateView(LoginRequiredMixin,UpdateView):
    model=Group
    template_name='expenses/edit_group.html'
    fields=['name']
    context_object_name='group'

    def get_success_url(self):
        return reverse_lazy('group_detail',kwargs={'pk':self.kwargs['pk']})
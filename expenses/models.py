from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name=models.CharField(max_length=200)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_groups')
    members=models.ManyToManyField(User,related_name='member_groups')

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    title=models.CharField(max_length=200)
    amount=models.IntegerField() #ruppees
    paid_by=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Split(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE,related_name='splits')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_owed = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} owes {self.amount_owed} for {self.expense}"
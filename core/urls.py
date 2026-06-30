"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from expenses import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('',views.GroupListView.as_view(),name='home'),
    path('group/create/',views.GroupCreateView.as_view(),name='create_group'),
    path('group/<int:pk>/detail/',views.GroupDetailView.as_view(),name='group_detail'),
    path('group/<int:pk>/add-expense/',views.ExpenseCreateView.as_view(),name='create_expense'),
    path('expense/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),
    path('split/<int:pk>/mark-paid/',views.mark_paid,name='mark_paid'),
    path('group/<int:pk>/del/',views.GroupDeleteView.as_view(),name='del_group'),
    path('expense/<int:pk>/del/',views.ExpenseDeleteView.as_view(),name='del_expense'),
    path('group/<int:pk>/edit/',views.GroupUpdateView.as_view(),name='edit_group'),
]

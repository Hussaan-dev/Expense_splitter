from rest_framework import serializers
from .models import Group,Expense,Split

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=['id','name','created_by','members']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=['id','title','amount','paid_by','group','created_at']

class SplitSerializer(serializers.ModelSerializer):
    class Meta:    
        model=Split
        fields=['id','expense','user','amount_owed','is_paid']

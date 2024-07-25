from django import forms
from .models import Income, Spending

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'description', 'category', 'amount']

class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ['date', 'description', 'category', 'amount']
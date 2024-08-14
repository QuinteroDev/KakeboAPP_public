from django import forms
from .models import Income, Spending

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'description', 'category', 'amount']
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError('Amount cannot be negative.')
        return amount

class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ['date', 'description', 'category', 'amount']
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError('Amount cannot be negative.')
        return amount
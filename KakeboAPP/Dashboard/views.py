from django.shortcuts import render, get_object_or_404, redirect
from .models import Income, Spending
from .forms import IncomeForm, SpendingForm
from django.utils.timezone import now
from datetime import datetime
from django.db import models

def dashboard(request):
    selected_year = request.GET.get('year', datetime.now().year)
    selected_month = request.GET.get('month', datetime.now().month)
    selected_year = int(selected_year)
    selected_month = int(selected_month)
    
    incomes = Income.objects.filter(date__year=selected_year, date__month=selected_month).order_by('date')
    spendings = Spending.objects.filter(date__year=selected_year, date__month=selected_month).order_by('date')
    
    total_income = incomes.aggregate(total=models.Sum('amount'))['total'] or 0
    total_spending = spendings.aggregate(total=models.Sum('amount'))['total'] or 0
    balance = total_income - total_spending

    income_form = IncomeForm()
    spending_form = SpendingForm()


    if request.method == 'POST':
        if 'add_income' in request.POST:
            income_form = IncomeForm(request.POST)
            if income_form.is_valid():
                if income_form.cleaned_data['amount'] < 0:
                    income_error_message = "The amount cannot be negative"
                else:
                    income_form.save()
                    return redirect('dashboard')
        elif 'add_spending' in request.POST:
            spending_form = SpendingForm(request.POST)
            if spending_form.is_valid():
                if spending_form.cleaned_data['amount'] < 0:
                    spending_error_message = "The amount cannot be negative"
                else:
                    spending_form.save()
                    return redirect('dashboard')
    
    context = {
        'incomes': incomes,
        'spendings': spendings,
        'total_income': total_income,
        'total_spending': total_spending,
        'balance': balance,
        'years': range(2024, 2027),
        'months': [
            {'value': 1, 'name': 'January'},
            {'value': 2, 'name': 'February'},
            {'value': 3, 'name': 'March'},
            {'value': 4, 'name': 'April'},
            {'value': 5, 'name': 'May'},
            {'value': 6, 'name': 'June'},
            {'value': 7, 'name': 'July'},
            {'value': 8, 'name': 'August'},
            {'value': 9, 'name': 'September'},
            {'value': 10, 'name': 'October'},
            {'value': 11, 'name': 'November'},
            {'value': 12, 'name': 'December'},
        ],
        'selected_year': selected_year,
        'selected_month': selected_month,
        'selected_month_display': datetime(selected_year, selected_month, 1).strftime('%B'),
        'income_form': income_form,
        'spending_form': spending_form,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['amount'] < 0:
                error_message = "The amount cannot be negative"
                context = {
                    'form': form,
                    'income_error_message': error_message
                }
                return render(request, 'dashboard/dashboard.html', context)
            else:
                form.save()
                return redirect('dashboard')
    else:
        form = IncomeForm()
    return redirect('dashboard')

def add_spending(request):
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['amount'] < 0:
                error_message = "The amount cannot be negative"
                context = {
                    'form': form,
                    'spending_error_message': error_message
                }
                return render(request, 'dashboard/dashboard.html', context)
            else:
                form.save()
                return redirect('dashboard')
    else:
        form = SpendingForm()
    return redirect('dashboard')

def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'dashboard/edit_income.html', {'form': form})

def edit_spending(request, pk):
    spending = get_object_or_404(Spending, pk=pk)
    if request.method == 'POST':
        form = SpendingForm(request.POST, instance=spending)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SpendingForm(instance=spending)
    return render(request, 'dashboard/edit_spending.html', {'form': form})

def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_income.html', {'income': income})

def delete_spending(request, pk):
    spending = get_object_or_404(Spending, pk=pk)
    if request.method == 'POST':
        spending.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_spending.html', {'spending': spending})
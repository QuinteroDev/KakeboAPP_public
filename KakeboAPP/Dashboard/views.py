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
    
    context = {
        'incomes': incomes,
        'spendings': spendings,
        'total_income': total_income,
        'total_spending': total_spending,
        'balance': total_income - total_spending,
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
        'selected_month_display': datetime(selected_year, selected_month, 1).strftime('%B')
    }
    
    return render(request, 'dashboard/dashboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'dashboard/add_income.html', {'form': form})

def add_spending(request):
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SpendingForm()
    return render(request, 'dashboard/add_spending.html', {'form': form})

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
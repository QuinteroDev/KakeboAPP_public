from django.shortcuts import render, get_object_or_404, redirect
from .models import Income, Spending
from .forms import IncomeForm, SpendingForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now



@login_required
def dashboard(request):
    months = [
        {'name': 'January', 'value': '01'},
        {'name': 'February', 'value': '02'},
        {'name': 'March', 'value': '03'},
        {'name': 'April', 'value': '04'},
        {'name': 'May', 'value': '05'},
        {'name': 'June', 'value': '06'},
        {'name': 'July', 'value': '07'},
        {'name': 'August', 'value': '08'},
        {'name': 'September', 'value': '09'},
        {'name': 'October', 'value': '10'},
        {'name': 'November', 'value': '11'},
        {'name': 'December', 'value': '12'},
    ]
    
    years = list(range(2024, 2027))  # Genera una lista de años desde 2024 hasta 2026
    
    selected_month = request.GET.get('month')
    selected_year = request.GET.get('year')
    if not selected_month or not selected_year:
        selected_month = now().strftime('%m')  # Formato: MM
        selected_year = now().strftime('%Y')  # Formato: YYYY

    year = int(selected_year)
    month = int(selected_month)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'income':
            date = request.POST.get('date')
            description = request.POST.get('description')
            category = request.POST.get('category')
            amount = request.POST.get('amount')
            Income.objects.create(user=request.user, date=date, description=description, category=category, amount=amount)
        elif form_type == 'spending':
            date = request.POST.get('date')
            description = request.POST.get('description')
            category = request.POST.get('category')
            amount = request.POST.get('amount')
            Spending.objects.create(user=request.user, date=date, description=description, category=category, amount=amount)
        return redirect('dashboard')

    incomes = Income.objects.filter(user=request.user, date__year=year, date__month=month)
    spendings = Spending.objects.filter(user=request.user, date__year=year, date__month=month)
    total_income = sum(income.amount for income in incomes)
    total_spending = sum(spending.amount for spending in spendings)
    selected_month_display = now().replace(year=year, month=month).strftime('%B')

    return render(request, 'dashboard/dashboard.html', {
        'incomes': incomes,
        'spendings': spendings,
        'total_income': total_income,
        'total_spending': total_spending,
        'selected_month': selected_month,
        'selected_year': selected_year,
        'selected_month_display': selected_month_display,
        'months': months,
        'years': years,
    })

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'dashboard/add_income.html', {'form': form})

@login_required
def add_spending(request):
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            spending = form.save(commit=False)
            spending.user = request.user
            spending.save()
            return redirect('dashboard')
    else:
        form = SpendingForm()
    return render(request, 'dashboard/add_spending.html', {'form': form})

@login_required
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

@login_required
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

@login_required
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_income.html', {'income': income})

@login_required
def delete_spending(request, pk):
    spending = get_object_or_404(Spending, pk=pk)
    if request.method == 'POST':
        spending.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_spending.html', {'spending': spending})
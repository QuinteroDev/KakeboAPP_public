# Analytics/views.py
from django.shortcuts import render
from Goals.models import UserGoal
from Dashboard.models import Spending, Income
from datetime import datetime
from django.db.models import Sum

def analytics_dashboard(request):
    user = request.user
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))

    # Obtener los objetivos del usuario
    goals = UserGoal.objects.all()

    # Obtener los ingresos y gastos del usuario para el mes y año seleccionados
    incomes = Income.objects.filter(date__year=year, date__month=month)
    total_income = incomes.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    spendings = Spending.objects.filter(date__year=year, date__month=month)

    # Calcular el total de gastos por categoría
    total_spendings = spendings.values('category').annotate(total_amount=Sum('amount'))

    # Comparación con los objetivos
    comparison = []
    for goal in goals:
        spending = next((item['total_amount'] for item in total_spendings if item['category'] == goal.category), 0)
        percentage_spent = (spending / total_income) * 100 if total_income > 0 else 0
        comparison.append({
            'category': goal.category,
            'goal_percentage': goal.percentage,
            'spending': spending,
            'percentage_spent': round(percentage_spent, 2),
            'status': calculate_status(goal.percentage, percentage_spent, goal.category)
        })

    balance = total_income - sum(item['spending'] for item in comparison)

    context = {
        'comparison': comparison,
        'total_income': total_income,
        'total_spending': sum(item['spending'] for item in comparison),
        'balance': balance,
        'selected_year': year,
        'selected_month': month,
        'selected_month_display': datetime(year, month, 1).strftime('%B'),  # Para mostrar el nombre del mes
        'years': range(2024, 2027),  # Ejemplo de rango de años
        'months': [
            {'value': 1, 'name': 'January'}, {'value': 2, 'name': 'February'}, {'value': 3, 'name': 'March'},
            {'value': 4, 'name': 'April'}, {'value': 5, 'name': 'May'}, {'value': 6, 'name': 'June'},
            {'value': 7, 'name': 'July'}, {'value': 8, 'name': 'August'}, {'value': 9, 'name': 'September'},
            {'value': 10, 'name': 'October'}, {'value': 11, 'name': 'November'}, {'value': 12, 'name': 'December'}
        ],
    }

    return render(request, 'analytics/dashboard.html', context)

def calculate_status(goal_percentage, percentage_spent, category):
    if percentage_spent == 0:
        return 'neutral'
    elif category == 'necesidades':
        if percentage_spent > goal_percentage:
            return 'red'
        else:
            return 'green'
    elif percentage_spent >= goal_percentage:
        return 'green'
    elif goal_percentage - percentage_spent <= 2:
        return 'green'
    elif 2 < goal_percentage - percentage_spent <= 5:
        return 'orange'
    else:
        return 'red'
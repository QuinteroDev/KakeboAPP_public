# Goals/views.py
from django.shortcuts import render, redirect
from .models import UserGoal
from django.contrib.auth.decorators import login_required


def goal_list(request):
    user_goals = UserGoal.objects.all()

    # Definir las categorías y los porcentajes predeterminados
    default_goals = [
        {'category': 'Basic Needs', 'percentage': 30},
        {'category': 'Savings and Investments', 'percentage': 10},
        {'category': 'Education', 'percentage': 10},
        {'category': 'Leisure', 'percentage': 10},
        {'category': 'Donations', 'percentage': 10},
        {'category': 'Projects and Entrepreneurship', 'percentage': 30},
    ]

    # Crear categorías predeterminadas si no existen

    user_goals = UserGoal.objects.all()

    if request.method == 'POST':
        total_percentage = 0
        for goal in user_goals:
            percentage = request.POST.get(f'percentage_{goal.id}')
            if percentage:
                total_percentage += int(percentage)
                goal.percentage = int(percentage)
        if total_percentage == 100:
            for goal in user_goals:
                goal.save()
            return redirect('goal_list')
        else:
            context = {
                'user_goals': user_goals,
                'error': 'The total percentage must equal 100%.'
            }
            return render(request, 'goals/goal_list.html', context)

    context = {
        'user_goals': user_goals,
    }
    return render(request, 'goals/goal_list.html', context)
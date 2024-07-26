from django.shortcuts import render, get_object_or_404, redirect
from .models import UserGoal
from .forms import UserGoalForm
from django.contrib.auth.decorators import login_required

@login_required
def goal_list(request):
    user_goals = UserGoal.objects.filter(user=request.user)

    if not user_goals.exists():
        default_goals = [
            {'category': 'Basic Needs', 'percentage': 30},
            {'category': 'Savings and Investment', 'percentage': 10},
            {'category': 'Education', 'percentage': 10},
            {'category': 'Entertainment', 'percentage': 10},
            {'category': 'Donations', 'percentage': 10},
            {'category': 'Projects and Entrepreneurship', 'percentage': 30},
        ]
        for goal in default_goals:
            UserGoal.objects.create(
                user=request.user,
                category=goal['category'],
                percentage=goal['percentage']
            )
        user_goals = UserGoal.objects.filter(user=request.user)

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

@login_required
def edit_goal(request, pk):
    goal = get_object_or_404(UserGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = UserGoalForm(instance=goal)
    return render(request, 'goals/goal_form.html', {'form': form})

@login_required
def delete_goal(request, pk):
    goal = get_object_or_404(UserGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goal_list')
    return render(request, 'goals/goal_confirm_delete.html', {'goal': goal})
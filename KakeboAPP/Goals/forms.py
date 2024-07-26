from django import forms
from .models import UserGoal

class UserGoalForm(forms.ModelForm):
    class Meta:
        model = UserGoal
        fields = ['category', 'percentage']

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if percentage < 0 or percentage > 100:
            raise forms.ValidationError("El porcentaje debe estar entre 0 y 100.")
        return percentage

    def clean(self):
        cleaned_data = super().clean()
        user = self.instance.user
        category = cleaned_data.get("category")
        percentage = cleaned_data.get("percentage")

        user_goals = UserGoal.objects.filter(user=user).exclude(category=category)
        total_percentage = sum(goal.percentage for goal in user_goals) + percentage
        if total_percentage > 100:
            raise forms.ValidationError("La suma total de los porcentajes no puede exceder el 100%.")
        return cleaned_data
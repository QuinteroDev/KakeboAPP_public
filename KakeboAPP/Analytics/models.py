from django.db import models
from django.conf import settings
from Goals.models import UserGoal  # Asegúrate de importar el modelo correcto

class MonthlyAnalytics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    category = models.CharField(max_length=100)
    total_spending = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ('user', 'year', 'month', 'category')

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.month}/{self.year}"

class SpendingGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    percentage = models.IntegerField()
    user_goal = models.ForeignKey(UserGoal, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.percentage}%"
# Analytics/models.py
from django.db import models

class MonthlyAnalytics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    category = models.CharField(max_length=100)
    total_spending = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('year', 'month', 'category')

    def __str__(self):
        return f"{self.category} - {self.month}/{self.year}"
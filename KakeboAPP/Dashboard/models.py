from django.db import models
import datetime
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0:
        raise ValidationError('Amount must be a positive number.')

class Spending(models.Model):
    SPENDING_CHOICES = (
        ('basic_needs', 'Basic Needs'),
        ('saving', 'Saving and Investment'),
        ('education', 'Education'),
        ('leisure', 'Leisure and Entertainment'),
        ('donations', 'Donations'),
        ('projects', 'Projects and Entrepreneurship'),
    )
    date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, choices=SPENDING_CHOICES, default='basic_needs')
    amount = models.FloatField(validators=[validate_positive]) 

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Income(models.Model):
    INCOME_CHOICES = (
        ('salary', 'Salary and Wages'),
        ('investments', 'Return on Investments'),
        ('projects', 'Project and Entrepreneurship Income'),
        ('other', 'Other Income'),
    )
    date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, choices=INCOME_CHOICES, default='salary')
    amount = models.FloatField(validators=[validate_positive])  

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.description} - {self.amount}"
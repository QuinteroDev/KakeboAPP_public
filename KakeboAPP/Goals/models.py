# Goals/models.py
from django.db import models

class UserGoal(models.Model):
    CATEGORY_CHOICES = (
        ('basic_needs', 'Basic Needs'),
        ('saving', 'Saving and Investment'),
        ('education', 'Education'),
        ('leisure', 'Leisure and Entertainment'),
        ('donations', 'Donations'),
        ('projects', 'Projects and Entrepreneurship'),
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    percentage = models.IntegerField()  

    def __str__(self):
        return f"{self.get_category_display()} ({self.percentage}%)"
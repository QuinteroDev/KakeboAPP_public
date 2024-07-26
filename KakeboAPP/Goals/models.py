# Goals/models.py
from django.db import models

class UserGoal(models.Model):
    CATEGORY_CHOICES = (
        ('necesidades', 'Necesidades Básicas'),
        ('ahorro', 'Ahorro e Inversión'),
        ('educacion', 'Formación y Educación'),
        ('ocio', 'Ocio y Entretenimiento'),
        ('donaciones', 'Donaciones'),
        ('proyectos', 'Proyectos y Emprendimiento'),
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    percentage = models.IntegerField()  

    def __str__(self):
        return f"{self.get_category_display()} ({self.percentage}%)"
from django.db import models
from django.conf import settings

class UserGoal(models.Model):
    CATEGORY_CHOICES = (
        ('necesidades', 'Necesidades Básicas'),
        ('ahorro', 'Ahorro e Inversión'),
        ('educacion', 'Formación y Educación'),
        ('ocio', 'Ocio y Entretenimiento'),
        ('donaciones', 'Donaciones'),
        ('proyectos', 'Proyectos y Emprendimiento'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    percentage = models.IntegerField()  

    class Meta:
        unique_together = ('user', 'category')

    def __str__(self):
        return f"{self.get_category_display()} ({self.percentage}%)"
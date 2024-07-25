# Dashboard/models.py

from django.db import models
from django.conf import settings
import datetime

class Spending(models.Model):
    SPENDING_CHOICES = (
        ('necesidades', 'Necesidades Básicas'),
        ('ahorro', 'Ahorro e Inversión'),
        ('educacion', 'Formación y Educación'),
        ('ocio', 'Ocio y Entretenimiento'),
        ('donaciones', 'Donaciones'),
        ('proyectos', 'Proyectos y Emprendimiento'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, choices=SPENDING_CHOICES, default='necesidades')
    amount = models.FloatField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.description} - {self.amount}"
    
# Dashboard/models.py

from django.db import models
from django.conf import settings
import datetime

class Income(models.Model):
    INCOME_CHOICES = (
        ('nomina', 'Nómina y Salarios'),
        ('inversiones', 'Retorno de Inversiones'),
        ('proyectos', 'Ingresos de Proyectos y Emprendimiento'),
        ('otros', 'Otros Ingresos'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, choices=INCOME_CHOICES, default='nomina')
    amount = models.FloatField()

    class Meta:
         ordering = ['date']

    def __str__(self):
        return f"{self.description} - {self.amount}"
from django.contrib import admin
from .models import Spending, Income

@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'category', 'amount']
    search_fields = ['description', 'category']
    list_filter = ['category']
    ordering = ['date']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'category', 'amount']
    search_fields = ['description', 'category']
    list_filter = ['category']
    ordering = ['date']
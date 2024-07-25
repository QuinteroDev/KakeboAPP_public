# Dashboard/admin.py

from django.contrib import admin
from .models import Spending, Income

@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'category', 'amount', 'user']
    search_fields = ['description', 'category', 'user__username']
    list_filter = ['category', 'user']
    ordering = ['date']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'category', 'amount', 'user']
    search_fields = ['description', 'category', 'user__username']
    list_filter = ['category', 'user']
    ordering = ['date']

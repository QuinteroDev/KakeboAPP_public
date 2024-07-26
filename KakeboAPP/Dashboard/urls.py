from django.urls import path
from .views import dashboard, add_income, add_spending, edit_income, edit_spending, delete_income, delete_spending

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add_income/', add_income, name='add_income'),
    path('add_spending/', add_spending, name='add_spending'),
    path('edit_income/<int:pk>/', edit_income, name='edit_income'),
    path('edit_spending/<int:pk>/', edit_spending, name='edit_spending'),
    path('delete_income/<int:pk>/', delete_income, name='delete_income'),
    path('delete_spending/<int:pk>/', delete_spending, name='delete_spending'),
]
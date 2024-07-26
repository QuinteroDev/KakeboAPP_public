# Goals/urls.py
from django.urls import path
from . import views
from .views import goal_list

urlpatterns = [
    path('', goal_list, name='goal_list'),
]
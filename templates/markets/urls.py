from django.urls import path
from . import views

urlpatterns = [
    path('markets/', views.markets_list, name='markets_list'),
]
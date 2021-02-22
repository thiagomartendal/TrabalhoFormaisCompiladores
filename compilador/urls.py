from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('editar_automato/', views.editarAutomato, name='editar_automato'),
]

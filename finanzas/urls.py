from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar_movimiento, name='agregar_movimiento'),
]
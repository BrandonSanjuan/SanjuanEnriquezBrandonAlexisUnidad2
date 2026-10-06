from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path(
        'agregar/',
        views.agregar_movimiento,
        name='agregar_movimiento'
    ),
    path(
        'eliminar/<int:id>/',
        views.eliminar_movimiento,
        name='eliminar_movimiento'
    ),
]
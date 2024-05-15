# en urls.py de la aplicación

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='main'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('profesores/', views.profesores, name='profesores'),
]

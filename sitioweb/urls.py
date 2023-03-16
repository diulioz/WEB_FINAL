from django.urls import path, include
from . import views
from sitio import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    # path('', views.inicio, name='inicio'),
    # path('nosotros', views.nosotros, name='nosotros'),
    path('', views.inicio, name='inicio'),
    path('todos', views.todos, name='todos'),
    path('agregar', views.agregar, name='agregar'),
    path('remover/<int:emp_id>', views.remover, name='remover'),
    path('remover', views.remover, name='remover'),
    path('filtrar', views.filtrar, name='filtrar'),
    path('autores', views.autores, name='autores'),
    path('salir/', views.salir, name="salir"),
]
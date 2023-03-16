from django.urls import path, include
from . import views
from sitio import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    # path('', views.inicio, name='inicio'),
    # path('nosotros', views.nosotros, name='nosotros'),
    path('', views.inicio, name='inicio'),
]
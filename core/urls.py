from django.urls import path
from .views import home, galeria, registro, registro_mascota

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('registro_mascota/', registro_mascota, name="registro_mascota"),
]
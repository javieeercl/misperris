from django.urls import path
from .views import home, galeria, registro

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
]
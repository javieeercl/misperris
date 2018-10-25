from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def registro(request):
    return render(request, 'core/registro.html')
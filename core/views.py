from django.shortcuts import render
from .models import *


from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

@login_required
def registro(request):
    regiones=Region.objects.all()
    ciudades=Ciudad.objects.all()
    viviendas=Vivienda.objects.all()
    variables={
        'regiones':regiones,
        'ciudades':ciudades,
        'viviendas':viviendas
    }

    if request.POST:
        adoptante=Adoptante()
        adoptante.run=request.POST.get('txtRut')
        adoptante.correo=request.POST.get('txtEmail')
        adoptante.nombre_completo=request.POST.get('txtNombreCompleto')        
        adoptante.f_nacimiento=request.POST.get('dtpFechaNacimiento')
        adoptante.telefono=request.POST.get('txtTelefono')

        region=Region() 
        region.id= int(request.POST.get('cboRegion'))
        adoptante.region=region 
        ciudad=Ciudad()
        ciudad.id= int(request.POST.get('cboCiudad'))
        adoptante.ciudad=ciudad
        vivienda=Vivienda()
        vivienda.id= int(request.POST.get('cboVivienda'))   
        adoptante.vivienda=vivienda

        try:
            adoptante.save()
            variables['mensaje']="Guardado Correctamente"
        except:
            variables['mensaje'] ="No se ha podido guardar "   

    return render(request,'core/registro.html',variables)

def registro_mascota(request):
    return render(request, 'core/registro_mascota.html')
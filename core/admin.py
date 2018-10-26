from django.contrib import admin
from .models import *

# Register your models here.

class AdoptanteAdmin(admin.ModelAdmin):
    list_display = ('run', 'correo', 'nombre_completo', 'f_nacimiento', 'telefono', 'region', 'ciudad', 'vivienda')
    search_fields=['run','nombre_completo']
    list_filter=('ciudad',)

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Vivienda)
admin.site.register(Adoptante, AdoptanteAdmin)
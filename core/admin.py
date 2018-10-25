from django.contrib import admin
from .models import Region, Ciudad, Vivienda, Adoptante

# Register your models here.

class AdoptanteAdmin(admin.ModelAdmin):
    list_display = ('run', 'nombre_completo', 'correo', 'f_nacimiento', 'telefono', 'region', 'ciudad', 'vivienda')

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Vivienda)
admin.site.register(Adoptante, AdoptanteAdmin)
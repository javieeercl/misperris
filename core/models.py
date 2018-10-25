from django.db import models

# Create your models here.

class Region(models.Model):
    id_region = models.IntegerField(unique=True)
    region = models.CharField(max_length=60)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name_plural = "Regiones"

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(unique=True)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=50) 

    def __str__(self):
        return self.ciudad
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Vivienda(models.Model):
    id_vivienda = models.IntegerField(unique=True)
    vivienda = models.CharField(max_length=60)

    def __str__(self):
        return self.vivienda

class Adoptante(models.Model):
    run =  models.CharField(max_length=12, unique=True)
    correo = models.CharField(max_length=60)
    nombre_completo = models.CharField(max_length=60)
    f_nacimiento = models.DateField()
    telefono = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.run
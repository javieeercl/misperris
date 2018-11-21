from django.db import models

# Create your models here.

class Region(models.Model):
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Regiones"

class Ciudad(models.Model):
    descripcion = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE) 

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Vivienda(models.Model):
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.descripcion

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
        return self.nombre_completo
    
    class Meta:
        verbose_name="Adoptante"    
        verbose_name_plural="Adoptantes"  

class Raza(models.Model):
    descripcion = models.CharField(max_length=60)
    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Razas"

class Estado(models.Model):
    descripcion = models.CharField(max_length=60)
    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Estados"

class Mascota(models.Model):
    nombre = models.CharField(max_length=60)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1)
    fecha_ingreso = models.DateField()
    fecha_nacimiento = models.DateField()
    descripcion = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="mascotas", null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
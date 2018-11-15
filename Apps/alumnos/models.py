from django.db import models

# Create your models here.

class alumnos(models.Model):
    Nombres: models.CharField(max_length=150)
    ApellidoPaterno: models.CharField(max_length=50)
    ApellidoMaterno: models.CharField(max_length=50)
    Rut: models.CharField(max_length=9)
    FechaNacimiento: models.DateField()

    def  __str__ (self):
        return "%s" %self.Nombres


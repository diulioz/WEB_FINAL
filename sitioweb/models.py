from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombreD = models.CharField(max_length=100, null=False)
    ubicacion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombreD

class Rol(models.Model):
    nombreR = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.nombreR

class Empleado(models.Model):
    nombreE = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100)
    dept = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    salario = models.IntegerField(default=0)
    bono = models.IntegerField(default=0)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    numeroCel = models.IntegerField(default=0)
    fechaContra = models.DateField()

    def __str__(self) -> str:
        return "%s %s %s" %(self.nombreE, self.apellido, self.numeroCel)
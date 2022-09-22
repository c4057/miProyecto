from django.db import models

# Create your models here. 

class Curso(models.Model):

    nombre = models.CharField(max_length=60) 
    camada = models.IntegerField() 

class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)

class Entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()

class Familiares(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    nacimiento = models.DateField()   

class Semillas(models.Model):
    nombre = models.CharField(max_length=60)

class Plantas(models.Model):
    nombre = models.CharField(max_length=60)

class Macetas(models.Model):
    nombre = models.CharField(max_length=60)
    modelo = models.IntegerField()
            







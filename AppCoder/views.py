from django.shortcuts import render
from django.template import Template, Context, loader
from datetime import datetime
from AppCoder.models import Curso, Entregable, Familiares
from django.http import HttpResponse

# Create your views here.

def curso(request): 
    materia = Curso(nombre="Hacking", camada=99999)

    materia.save()

    return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")

def entregables(request):

    ente1 = Entregable(nombre="Examen 1", fechaEntrega = "2022-08-09")

    ente1.save() #guadar en base de datos

    return HttpResponse(f"He guardado: {ente1.nombre} con fecha {ente1.fechaEntrega}")

def familiares(request):

    fam3 = Familiares(nombre="Ines", edad=60, nacimiento="1961-05-30") 
    fam3.save()
        
    fam2 = Familiares(nombre="Carlos", edad=62, nacimiento="1959-07-10")
    fam2.save()

    fam1 = Familiares(nombre="Fernanda", edad=42, nacimiento="1980-11-08")   
    fam1.save()
    
    
    documentoDeTexto = f" Esta es mi familia. Mi mama se llama {fam3.nombre}, tiene {fam3.edad} y nació el {fam3.nacimiento}. Mi papá se llama {fam2.nombre}, tiene {fam2.edad} y nació el {fam2.nacimiento}). Mi hermana se llama {fam3.nombre}, tiene {fam3.edad} y nació el {fam3.nacimiento}"
    

    return HttpResponse(documentoDeTexto) 


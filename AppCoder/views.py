from django.shortcuts import render
from django.template import Template, Context, loader
from datetime import datetime
from AppCoder.models import *
from AppCoder.forms import * 
from django.http import HttpResponse





# Create your views here.

def inicio (request):
    #return HttpResponse ("Esta es la vista de bienvenida.")
    return render (request, "AppCoder/inicio.html")



def curso(request): 
    materia = Curso(nombre="Hacking", camada=99999)

    materia.save()

    #return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")
    return render (request, "AppCoder/cursos.html")

def estudiante (request): 
    
    #return HttpResponse(f"Esta es la vista de los estudiantes.")
    return render (request, "AppCoder/estudiantes.html")


def profesores (request): 
    
    #return HttpResponse(f"Esta es la vista de los profesores.")
    return render (request, "AppCoder/profesores.html")


def entregables(request):

    ente1 = Entregable(nombre="Examen 1", fechaEntrega = "2022-08-09")

    ente1.save() #guadar en base de datos

    #return HttpResponse(f"He guardado: {ente1.nombre} con fecha {ente1.fechaEntrega}")
    return render (request, "AppCoder/entregables.html")


def familiares(request):

    fam3 = Familiares(nombre="Ines", edad=60, nacimiento="1961-05-30") 
    fam3.save()
        
    fam2 = Familiares(nombre="Carlos", edad=62, nacimiento="1959-07-10")
    fam2.save()

    fam1 = Familiares(nombre="Fernanda", edad=42, nacimiento="1980-11-08")   
    fam1.save()
    
    
    documentoDeTexto = f" Esta es mi familia. Mi mama se llama {fam3.nombre}, tiene {fam3.edad} y nació el {fam3.nacimiento}. Mi papá se llama {fam2.nombre}, tiene {fam2.edad} y nació el {fam2.nacimiento}). Mi hermana se llama {fam3.nombre}, tiene {fam3.edad} y nació el {fam3.nacimiento}"
    

    return HttpResponse(documentoDeTexto) 

def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioCurso(request.POST) # se toma la info de html 
        

        if formulario1.is_valid (): # comprueba que no haya errores

            info = formulario1.cleaned_data
        
            cursoF = Curso(nombre=info["curso"], camada=info["camada"])  #request.POST["curso"], camada=request.POST["camada"]) # lee la info de las cajas de texto

            cursoF.save() # guarda en la base de datos

            return render(request, "AppCoder/inicio.html") # ocurre al dar click en GO, usamos metodo post, vuelve a mostrar la pag del formulario, pero vacío.


    else: 

        formulario1=FormularioCurso() # mostrar el formulario vacio


    return render(request, "AppCoder/formu1.html", {"form1":formulario1}) # entro al url y me muestra esta plantilla despues de dar click al boton, op 2 es crear un diccionario



def formulario2(request):

    if request.method=="POST":

        formulario2 = FormularioProfe(request.POST) # se toma la info de html 
        

        if formulario2.is_valid (): # comprueba que no haya errores

            info = formulario2.cleaned_data
        
            profeF = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])  #request.POST["curso"], camada=request.POST["camada"]) # lee la info de las cajas de texto

            profeF.save() # guarda en la base de datos

            return render(request, "AppCoder/inicio.html") # ocurre al dar click en GO, usamos metodo post, vuelve a mostrar la pag del formulario, pero vacío.


    else: 

        formulario2=FormularioProfe() # mostrar el formulario vacio


    return render(request, "AppCoder/formu2.html", {"form2":formulario2})



def busquedaCursos(request):

    return render(request, "AppCoder/busquedaCursos.html") 

def buscar(request):

    if request.GET["camada"]: # si la info existe

        busqueda = request.GET["camada"] #traigo la info
        cursos = Curso.objects.filter(camada__icontains=busqueda) # todos los objetos creados en el modelo Cursos, los voy a filtrar

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "busqueda":busqueda}) # cambie resultados.html por inicio.html, creamos un template nuevo en el que me muestra los rsultados 

    else: # si no se colocaron datos

        mensaje = "No enviaste datos."


    #busqueda = request.GET["camada"] sirve para primera opción


    #return HttpResponse(f"Estoy buscando la camada número: {busqueda}")  sirve para primera opción     

    return HttpResponse(mensaje)


def semillas(request):
   sem1 = Semillas(nombre="Espinaca") 

   sem1.save()

   sem2 = Semillas(nombre="Cebolla")
   sem2.save()

   sem3 = Semillas(nombre="Remolacha")
   sem3.save()

   return render (request, "AppCoder/semillas.html")

def plantas(request):
   plan1 = Plantas(nombre="Ficus") 
   plan1.save()

   plan2 = Plantas(nombre="Monstera")
   plan2.save()

   plan3 = Plantas(nombre="Potus")
   plan3.save()

   return render (request, "AppCoder/plantas.html")
   
   
def macetas(request):

   mac1 = Macetas(nombre="Terracota", modelo=123) 

   mac1.save()

   mac2 = Macetas(nombre="Cemento", modelo=124)
   mac2.save()

   mac3 = Macetas(nombre="Cerámica", modelo=125)
   mac3.save()

   return render (request, "AppCoder/macetas.html")
    

        
def formulariosem(request):

    if request.method== "POST":
        
        formulariosem= FormularioSem(request.POST)

        if formulariosem.is_valid():

            info = formulariosem.cleaned_data

            formsem = Semillas(nombre=info["nombre"]) 

            formsem.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulariosem = FormularioSem()       


    return render(request, "AppCoder/formsem.html", {"formsem1":formulariosem})


def formularioplan(request):

    if request.method== "POST":

        formplan= Plantas(nombre=request.POST["plantas"])

        formplan.save()

        return render (request, "AppCoder/inicio.html")

    return render(request, "AppCoder/formplan.html")    

def formulariomac(request):

    if request.method== "POST":

        formmac= Macetas(nombre=request.POST["macetas"], modelo=request.POST["modelo"])

        formmac.save()

        return render (request, "AppCoder/inicio.html")

    return render(request, "AppCoder/formmac.html")

def busquedaModelo (request): # buscar modelos de macetas
    
    return render(request, "AppCoder/busquedaModelo.html")

def buscamod (request):   # para mostrar los resultados  

    if request.GET["modelo"]: # si estoy buscando el modelo

        modelo = request.GET["modelo"]     #quiero saber el modelo buscado  

        maceta = Macetas.objects.filter(modelo__iexact=modelo)

        return render(request, "AppCoder/buscamod.html", {"maceta":maceta, "modelo":modelo})

    else: 

        respuesta = "No se han enviado datos"     
    
       
    return HttpResponse (respuesta)

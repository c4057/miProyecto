from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", curso, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("entregables/", entregables, name="Entregables"),
    path("familiares/", familiares),
    path("form1/", formulario1),
    path("form2/", formulario2),
    path("buscarCursos/", busquedaCursos),
    path("buscar/", buscar),
    path("semillas/", semillas, name="Semillas"),
    path("plantas/", plantas, name="Plantas"),
    path("macetas/", macetas, name="Macetas"),
    path("formsem/", formulariosem, name="semillasformulario"),
    path("formplan/", formularioplan, name="plantasformulario"),
    path("formmac/", formulariomac, name="macetasformulario"),
    path("buscarModelo/", busquedaModelo, name="BuscarModelo"),
    path("buscamod/", buscamod, name="ResultadosBusqueda"), 
]

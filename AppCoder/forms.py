from django import forms

class FormularioCurso(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class FormularioProfe(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class FormularioSem(forms.Form):
    nombre = forms.CharField()

class FormularioPlan(forms.Form):
    nombre = forms.CharField()

class FormularioMac(forms.Form):
    nombre = forms.CharField()
    modelo = forms.IntegerField()        
       

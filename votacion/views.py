from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from votacion.forms import VotacionForm
from votacion.models import Votacion

from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def votacion(request):
    votacion = Votacion.objects.all
    return render(request,'votacion/index.html',{'votacion':votacion})

def crear(request):
    formulario = VotacionForm(request.POST or None,request.FILES or None)
    #CUANDO EL FORMULARIO SE ENVIA CON DATOS       
    
    if request.method == 'POST':     
        jurado = formulario.data['jurado'] or None
        degustador = formulario.data['degustador'] or None
        muestra = formulario.data['muestra'] or None
        registro = Votacion.objects.filter(jurado=jurado).filter(degustador=degustador).filter(muestra=muestra)
        if registro:
            messages.warning(request,'Error, ya se registro una votacion para el mismo jurado, degustrador y muestra.')
            return redirect('crear')

    if formulario.is_valid():
        formulario.save()
        return redirect('crear')
    return render(request,'votacion/crear.html',{'formulario':formulario})
    
def eliminar(request,id):
    return redirect('votacion')

def editar(request,id)  :
    formulario=VotacionForm(request.POST or None,request.FILES or None,instance=votacion)
    return render(request,'votacion/editar.html',{'formulario':formulario})

    
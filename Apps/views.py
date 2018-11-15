from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'home.html')

@login_required()
def registroAlumno(request):
	return render(request, 'registroAlumno.html')

@login_required()
def AdministradorArchivo(request):
	return render(request, 'AdministradorArchivo.html')
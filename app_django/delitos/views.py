from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'delitos/header.html')
def sesion(request):
    return render(request, 'delitos/sesion.html')
def registro(request):
    return render(request, 'delitos/registro.html')
def historial(request):
    return render(request, 'delitos/historial.html')

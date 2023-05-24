from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'usuarios/principal.html')
def denuncia(request):
    return render(request, 'usuarios/denuncia.html')

"""
URL configuration for app_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from delitos import views as views_delitos
from usuarios import views as views_usu


urlpatterns = [
    path('', views_delitos.home, name='home'),
    path('sesion/', views_delitos.sesion,name = 'sesion'),
    path('registro/', views_delitos.registro,name = 'registro'),
    path('historial/delitos/', views_delitos.historial,name = 'historial'),
    path('usuarios/denuncia/', views_usu.denuncia,name = 'denuncia'),
    path('usuarios/inicio/', views_usu.home,name = 'inicio'),
    path('admin/', admin.site.urls),
]


"""
URL configuration for startapp project.

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
from django.http import HttpResponse


from cursos.views import cursos, cursos_api, show_form

def holamundo(request):
    print(request)
    print(request.headers)
    return HttpResponse('<h1>Hola desde url.py</h1>')

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse(f'<center>Hola { nombre }</center>')

def suma(request , n1, n2):
    resultado = n1 + n2
    return HttpResponse('El resultado es: ' + str(resultado))

urlpatterns = [
    path('holamundo/', holamundo),
    path('cursos/', cursos),
    path('cursos/api/', cursos_api),
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('suma/<int:n1>/<int:n2>', suma),
    path('formulario', show_form),
]

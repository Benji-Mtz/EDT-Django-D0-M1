from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Importamos el modelo de la tabla Curso
from .models import TblCurso

# Create your views here.
# funciones como vistas para el url.py

def cursos(request):
    # Traemos todos los cursos que tenemos en la BD
    lista_cursos = TblCurso.objects.all()
    print(f'Lista de cursos: {lista_cursos}')
    
    str_cursos = "<ul>\n"
    
    for curso in lista_cursos:
        str_cursos += f'<li>{curso.curso_titulo}</li>'
    
    str_cursos += "</ul>"
    return HttpResponse('<center><h1>Mi curso edteam</h1></center><br>' + str_cursos)

def cursos_api(request):
    lista_cursos = TblCurso.objects.all()
    lista_final = []
    
    for curso in lista_cursos:
        dict_curso = {
            'id': curso.curso_id,
            'titulo': curso.curso_titulo,
            'descripcion': curso.curso_descripcion,
        }
        lista_final.append(dict_curso)
    
    data_json = {
        'data': lista_final
    }
    return JsonResponse(data_json)

def show_form(req):
    result = 0
    if req.method == 'POST':
        n1 = int(req.POST['n1'])
        n2 = int(req.POST['n2'])
        
        result = n1 + n2
        
    context = {
        'result': result
    }
    return render(req, 'formulario.html', context)
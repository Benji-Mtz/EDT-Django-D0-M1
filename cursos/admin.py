from django.contrib import admin

# Register your models here.
from .models import TblCurso, TblCategoria

# Damos de alta en el admin estas tablas
admin.site.register(TblCurso)
admin.site.register(TblCategoria)
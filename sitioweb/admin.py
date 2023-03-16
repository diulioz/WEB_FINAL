from django.contrib import admin
from .models import Empleado, Rol, Departamento

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Departamento)

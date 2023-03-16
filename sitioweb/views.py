from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado, Departamento, Rol
from django.db.models import Q
# from .forms import LibroForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib import messages
from datetime import datetime

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def autores(request):
    return render(request, 'autores.html')

def todos(request):
    empleados = Empleado.objects.all()
    informacion = {
        'empleados': empleados
    }
    return render(request, 'todos.html', informacion)

def agregar(request):
    if request.method == 'POST':
        nombreE = request.POST['nombreE']
        apellido = request.POST['apellido']
        salario = int(request.POST['salario'])
        bono = int(request.POST['bono'])
        numeroCel = int(request.POST['numeroCel'])
        dept = int(request.POST['dept'])
        rol = int(request.POST['rol'])
        empNuevo = Empleado(nombreE=nombreE, apellido=apellido, salario=salario, bono=bono, numeroCel=numeroCel, dept_id = dept, rol_id=rol, fechaContra=datetime.now())
        empNuevo.save()  
        return HttpResponse('Empleado Agregado Correctamente')  
    elif request.method=='GET':
        return render(request, 'agregar.html')
    else:
        return HttpResponse('Ha ocurrido un problema')  

def remover(request, emp_id=0):
    if emp_id:
        try:
            empRemover = Empleado.objects.get(id=emp_id)
            empRemover.delete()
            return HttpResponse("Eliminación correcta")
        except:
            return HttpResponse("Entre un ID correcto")
    empleados = Empleado.objects.all()
    informacion = {
        'empleados':empleados
    }

    return render(request, 'remover.html', informacion)

def filtrar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        dept = request.POST['dept']
        rol = request.POST['rol']
        empleados = Empleado.objects.all()
        if nombre:
            empleados = empleados.filter(Q(nombreE__icontains = nombre) | Q(apellido__icontains = nombre))
        if dept:
            empleados = empleados.filter(dept__nombreD__icontains = dept)
        if rol:
            empleados = empleados.filter(rol__nombreR__icontains = rol)

        informacion = {
        'empleados':empleados
        }
        return render(request, 'todos.html', informacion)
    elif request.method=='GET':
        return render(request, 'filtrar.html')
    else:
        return HttpResponse('Ha ocurrido un problema')
    



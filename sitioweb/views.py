from django.shortcuts import render
from django.http import HttpResponse
# from .models import libro
# from .forms import LibroForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')
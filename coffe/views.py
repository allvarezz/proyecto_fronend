from django.shortcuts import render
from .models import Producto

# Create your views here.

def index(request):

    return render(request,'coffe/index.html')

def producto(request):
    productos=Producto.objects.all()

    return render(request,'coffe/productos.html',{
        'productos':productos
    })

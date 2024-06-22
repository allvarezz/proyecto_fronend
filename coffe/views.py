from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'coffe/index.html')

def producto(request):

    return render(request,'coffe/productos.html')

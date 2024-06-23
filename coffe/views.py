from django.shortcuts import render,redirect
from .models import Producto
from .forms import FormProd

# Create your views here.

def index(request):

    return render(request,'coffe/index.html')

def producto(request):
    productos=Producto.objects.all()

    return render(request,'coffe/productos.html',{
        'productos':productos
    })

def list_prod(request):
     productos=Producto.objects.all()

     return render(request,'coffe/listado_prod.html',{'productos':productos})

def add_prod(request):
    if request.method == 'POST':
        form=FormProd(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
            form=FormProd()
    return render(request,'coffe/adm_add_prod.html',{'form':form})
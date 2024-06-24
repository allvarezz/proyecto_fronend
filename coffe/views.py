from django.shortcuts import render,redirect
from .models import Producto
from .forms import FormProd

# Create your views here.

def index(request):

    return render(request,'coffe/index.html')

def Ext_prod(request):
     productos=Producto.objects.all()
     return productos

def producto(request):
    productos=Producto.objects.all()

    return render(request,'coffe/productos.html',{
        'productos':productos
    })

def list_prod(request):
     productos=Producto.objects.all()

     return render(request,'coffe/listado_prod.html',{'productos':productos})

def del_prod(request,id):
     
        try:
          productos=Producto.objects.all()
          producto=Producto.objects.get(id_producto=int(id))
          producto.delete()
          return render(request,'coffe/listado_prod.html',{'productos':productos})
        except:
             return render(request,'coffe/listado_prod.html',{'productos':productos})

def edi_prod(request,id):
        try:
          productos=Producto.objects.all()
          producto=Producto.objects.get(id_producto=int(id))
          if producto:
               if request.method == 'POST':
                    form=FormProd(request.POST,instance=producto)
                    form.save()
          return redirect('BD')
        except:
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
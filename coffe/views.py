from django.shortcuts import render, redirect
from .models import Producto,Categoria
from .forms import FormProd, ContactoForm

# Create your views here.


def index(request):

    return render(request, 'coffe/index.html')


def Ext_prod():
     productos = Producto.objects.all()
     return productos


def producto(request):
    if request:
        return render(request, 'coffe/productos.html', {
            'productos': Ext_prod()
        })
    
def N_categoria(request):
     
     categorias=Categoria.objects.all()
     
     
     return render(request,'coffe/N_categoria.html',{'categorias':categorias,'true':True,'productos':Ext_prod()})

def N_cat_prod(request,id):
     
     categorias=Categoria.objects.all()
     producto_categoria=Producto.objects.filter(fk_categoria=id)
     
     return render(request,'coffe/N_categoria.html',{'producto':producto_categoria,'categorias':categorias})


def list_prod(request):
     orden = request.GET.get('orden', 'id_producto')
     productos = Producto.objects.all().order_by(orden)
     if request:
          if request.method == 'POST':
            form = FormProd(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect('BD')
          form = FormProd()
     return render(request, 'coffe/listado_prod.html', {'productos': productos, 'form': form})


def del_prod(request, id):

        try:
          producto = Producto.objects.get(id_producto=int(id))
          producto.delete()
          return render(request, 'coffe/listado_prod.html', {'productos': Ext_prod()})
        except:
             return render(request, 'coffe/listado_prod.html', {'productos': Ext_prod()})


def edi_prod(request, id):
        try:
          producto = Producto.objects.get(id_producto=int(id))
          if producto:
               if request.method == 'POST':
                    form = FormProd(request.POST, instance=producto)
                    form.save()
          return redirect('BD')
        except:
             return render(request, 'coffe/listado_prod.html', {'productos': Ext_prod()})


def add_prod(request):
    if request.method == 'POST':
        form = FormProd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
            form = FormProd()
    return render(request, 'coffe/adm_add_prod.html', {'form': form})


def cruD(request):
    if request.method == 'POST':
        form = FormProd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('BD')
    else:
            form = FormProd()
    return render(request, 'coffe/listado_prod.html', {'form': form})


def contac(request):
     if request.method == 'POST':
           form = ContactoForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect('contacto')
     else:
            form=ContactoForm()
     return render(request,'coffe/contacto.html',{
     'forms':form
})




     
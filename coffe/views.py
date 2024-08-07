from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .models import Producto,Categoria
from .forms import FormProd, ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def index(request):
    return render(request, 'coffe/index.html')
def menu(request):
    return render(request, 'coffe/menu.html')
def contacto(request):
     if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']

        template = render_to_string('email.html', {
            'nombre': nombre,
            'correo': correo,
            'mensaje': mensaje
        })

        try:
            emailSender = EmailMessage(
                'Contacto desde la página web',  # Asunto del correo
                template,
                settings.EMAIL_HOST_USER,
                ['juan.alvarez.g.97@gmail.com', 'ju.alvarezg@duocuc.cl']
            )
            emailSender.content_subtype = 'html'
            emailSender.fail_silently = False
            emailSender.send()
            messages.success(request, 'Correo enviado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al enviar el correo: {e}')

        return redirect('index')
     
     return render(request, 'coffe/contact.html')


def salir(request):
     logout(request)
     return redirect('index')

def login(request):
    
    return render(request,'registration/login.html')

def about(request):
   
     return render(request,'coffe/about.html')


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
               else:
                form=FormProd(instance=producto)
                return render(request, 'coffe/listado_prod.html', {'productos': Ext_prod(),'edi_form':form})
        except:
             return render(request, 'coffe/listado_prod.html', {'productos': Ext_prod(),'edi_form':form})
        



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




@login_required
def pedidos(request):
     categorias=Categoria.objects.all()

     

     return render(request,'coffe/pedido.html',{'categorias':categorias,'true':True,'productos':Ext_prod()})

def pedidosP(request,id):
     
     categorias=Categoria.objects.all()
     producto_categoria=Producto.objects.filter(fk_categoria=id)
     
     return render(request,'coffe/pedido.html',{'producto':producto_categoria,'categorias':categorias})




     
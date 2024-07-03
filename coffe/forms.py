from django import forms
from .models import Producto ,Contacto


class FormProd(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['nombre', 'imagen', 'descripcion', 'precio', 'fk_categoria']
        labels={'fk_categoria':'Categoria'}

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields='__all__'


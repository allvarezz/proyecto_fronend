from django import forms
from .models import Producto


class FormProd(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['nombre', 'imagen', 'descripcion', 'precio', 'fk_categoria']
        labels={'fk_categoria':'Categoria'}


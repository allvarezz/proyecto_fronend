from django.db import models

# Create your models here.
class Categoria(models.Model):

    id_categoria =models.AutoField(db_column='idCate',primary_key=True)
    nombre=models.CharField(max_length=35)
    def __str__(self):
        return str(self.nombre)



class Producto(models.Model):

    id_producto=models.AutoField(db_column='idProd',primary_key=True)
    nombre=models.CharField(max_length=350)
    imagen=models.ImageField(upload_to='upload')
    descripcion=models.CharField(max_length=400)
    precio=models.IntegerField()
    fk_categoria=models.ForeignKey('Categoria',on_delete=models.CASCADE,db_column='idCate')



    def __str__(self):
        return str(self.nombre)

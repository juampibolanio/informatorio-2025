from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
class Noticia(models.Model):
    noticia_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80) 
    subtitulo = models.CharField(max_length= 150)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=50, null=True)
    imagen = models.ImageField()
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo
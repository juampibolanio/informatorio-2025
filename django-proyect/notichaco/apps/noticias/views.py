from django.shortcuts import render
from .models import Autor, Categoria, Noticia

#CREATE

def crear_noticia(request):
    
    cat = Categoria.objects.get(categoria_id = 1)
    autor = Autor.objects.get(autor_id = 1) 
    
    nueva_noticia = Noticia(
        titulo = "Noticia en clase 1",
        subtitulo = "Subtitulo de prueba",
        contenido = "este es un contenido de prueba para la nueva noticia :D",
        autor = autor
    )

    nueva_noticia.save()

    nueva_noticia.categoria.set([cat])

    print("=========================")
    print(nueva_noticia.titulo)
    print(nueva_noticia.subtitulo)
    print(nueva_noticia.contenido)
    print(nueva_noticia.autor)

    return render(request, 'nueva_noticia.html')

#UPDATE

def modificar_noticia(request):

    noticia_actual = Noticia.objects.filter(titulo = "Noticia en clase 1").first()

    noticia_actual.titulo = "Noticia MODIFICADA"
    noticia_actual.subtitulo = "Subtitulo modificado"
    noticia_actual.contenido = "CONTENIDO DE LA NOTICIA MODIFICADO"

    noticia_actual.save()

    print("=========================")
    print(noticia_actual.titulo)
    print(noticia_actual.subtitulo)
    print(noticia_actual.contenido)
    print(noticia_actual.autor)
    print("=========================")


    return render(request, 'modificar_noticia.html')
        

#DELETE
def eliminar_noticia(request):

    noticia = Noticia.objects.get(noticia_id = 3)
    noticia.delete()
    print("SE ELIMINO LA NOTICIA CORRECTAMENTE")
    
    return render(request, 'eliminar_noticia.html')


#Rutas READ
# Create your views here.
def todas_las_noticias(request):

    noticias = Noticia.objects.all()

    for noticia in noticias:
        print("****************")
        print(noticia.titulo)
        print(noticia.subtitulo)
        print(noticia.autor)

    return render(request, 'todas_noticias.html')

def una_noticia(request):

    noticia = Noticia.objects.get(noticia_id = 1)
    print(noticia.titulo)
    print(noticia.contenido)

    return render(request, 'una_noticia.html')

def noticia_categoria(request):

    noticias_politica = Noticia.objects.filter(categoria__nombre = "Politica")
    print("Noticias en categoría Politica")

    for noticia in noticias_politica:
        print(noticia.titulo)
        print(noticia.contenido)
        print(f"escrito por {noticia.autor}")

    return render(request, 'politica_noticias.html')
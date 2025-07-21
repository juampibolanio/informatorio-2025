from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Autor, Categoria, Noticia


#====================== VISTAS BASADAS EN CLASES ===========================

class TodasLasNoticiasView(ListView):
    model = Noticia
    template_name = 'todas_noticias.html'
    context_object_name = 'noti'

class UnaNoticiaView(DetailView):
    model = Noticia
    template_name = 'una_noticia.html'
    context_object_name = 'noticia'
    pk_url_kwarg = 'noticia_id'

class CrearNoticiaView(CreateView):
    model = Noticia
    template_name = 'nueva_noticia.html'
    fields = ['titulo', 'subtitulo', 'contenido']
    success_url = reverse_lazy('todas_las_noticias') #ESTE METODO HAY Q COMPLETAR LA SEMANA Q VIENE, PQ TIENE TEMAS SOBRE FORMULARIOS

class ActualizarNoticiaView(UpdateView):
    model = Noticia
    template_name = 'modificar_noticia.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('todas_las_noticias')
    pk_url_kwarg = 'noticia_id'

class EliminarNoticiaView(DeleteView):
    model = Noticia
    template_name = 'eliminar_noticia.html'
    success_url = reverse_lazy('todas_las_noticias')
    pk_url_kwarg = 'noticia_id'

#====================== VISTAS BASADAS EN FUNCIONES ========================
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

    context = {
        'noticias' : noticias
    }

    return render(request, 'todas_noticias.html', context)

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
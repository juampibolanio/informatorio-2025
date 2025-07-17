from django.urls import path

from apps.noticias.views import noticia_categoria_politica, todas_las_noticias, una_noticia

urlpatterns = [
    path('todas/', todas_las_noticias, name='todas_las_noticias'),
    path('una/', una_noticia, name='una_noticia'),
    path('politica/', noticia_categoria_politica, name='noticia_categoria_politica'),
]
from django.urls import path

from apps.noticias.views import crear_noticia, eliminar_noticia, modificar_noticia, noticia_categoria, todas_las_noticias, una_noticia

urlpatterns = [

    #Rutas READ
    path('', todas_las_noticias, name='todas_las_noticias'),
    path('detalle/', una_noticia, name='una_noticia'),
    path('categoria/', noticia_categoria, name='noticia_categoria'),
    path('crear/', crear_noticia, name = 'crear_noticia'), #CREATE 
    path('editar/', modificar_noticia, name = 'modificar_noticia'), #UPDATE
    path('eliminar/', eliminar_noticia, name = 'eliminar_noticia') #DELETE
]
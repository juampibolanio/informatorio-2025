from django.urls import path

from apps.noticias.views import ActualizarNoticiaView, CrearNoticiaView, EliminarNoticiaView, TodasLasNoticiasView, UnaNoticiaView, crear_noticia, eliminar_noticia, modificar_noticia, noticia_categoria, todas_las_noticias, una_noticia

urlpatterns = [

    #Rutas PARA VISTAS X CLASES

    #READ
    path('', TodasLasNoticiasView.as_view(), name = 'todas_las_noticias'),
    path('detalle/<int:noticia_id>', UnaNoticiaView.as_view(), name='una_noticia'),
    path('crear/', CrearNoticiaView.as_view(), name='crear_noticia'),
    path('editar/<int:noticia_id>', ActualizarNoticiaView.as_view(), name='modificar_noticia'),
    path('eliminar/<int:noticia_id>', EliminarNoticiaView.as_view(), name='eliminar_noticia'),

    #Rutas PARA VISTAS X FUNCIONES READ
    #path('', todas_las_noticias, name='todas_las_noticias'),
    #path('detalle/', una_noticia, name='una_noticia'),
    path('categoria/', noticia_categoria, name='noticia_categoria'),
    #path('crear/', crear_noticia, name = 'crear_noticia'), #CREATE 
    #path('editar/', modificar_noticia, name = 'modificar_noticia'), #UPDATE
    #path('eliminar/', eliminar_noticia, name = 'eliminar_noticia') #DELETE
]
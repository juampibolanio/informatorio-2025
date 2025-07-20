from django.contrib import admin
from .models import Noticia, Categoria, Autor

#Personalizaciones
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'autor')

    list_filter = ('fecha', 'autor', 'categoria')

    search_fields = ('titulo', 'autor')

# Register your models here.

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)
admin.site.register(Autor)
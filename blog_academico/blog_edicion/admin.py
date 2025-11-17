from django.contrib import admin
from .models import Articulo, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
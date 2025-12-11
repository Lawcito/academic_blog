from django.contrib import admin

# Importamos TODOS los modelos para que no falte ninguno
from .models import Apunte, Articulo, Carrera, Materia, Evento

# ==========================================
# 1. CONFIGURACIÓN ESTRUCTURA (Carreras y Materias)
# ==========================================
admin.site.register(Carrera)


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "carrera", "año")
    list_filter = ("carrera",)


# ==========================================
# 2. CONFIGURACIÓN CALENDARIO (Nuevo)
# ==========================================
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha")
    ordering = ("fecha",)


# ==========================================
# 3. PANEL DE APUNTES (De tus compañeros)
# ==========================================
@admin.register(Apunte)
class ApunteAdmin(admin.ModelAdmin):
    # Qué columnas se ven en la lista
    list_display = ("titulo", "materia", "tipo", "autor", "fecha_subida")
    # Filtros laterales (barra derecha)
    list_filter = ("tipo", "materia", "fecha_subida")
    # Barra de búsqueda (Agregué __nombre para que busque por el nombre de la materia)
    search_fields = ("titulo", "materia__nombre", "descripcion")


# ==========================================
# 4. PANEL DE ARTÍCULOS (Tu parte)
# ==========================================
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    # Qué columnas se ven en la lista
    list_display = ("titulo", "autor", "fecha_publicacion")
    # Filtros laterales
    list_filter = ("fecha_publicacion", "autor")
    # Barra de búsqueda (busca en título y en el cuerpo de la noticia)
    search_fields = ("titulo", "cuerpo", "bajada")
    # Navegación por fechas arriba de la lista
    date_hierarchy = "fecha_publicacion"

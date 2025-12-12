from django.urls import path
from . import views

app_name = "blog_edicion"

urlpatterns = [
    # --- Noticias ---
    path("", views.ver_todas_noticias, name="ver_todas_noticias"),
    path("todas/", views.ver_todas_noticias, name="ver_todas_noticias"),
    path("crear/", views.crear_articulo, name="crear_articulo"),
    path("detalle/<int:pk>/", views.articulo_detalle, name="articulo_detalle"),
    path("editar/<int:pk>/", views.editar_articulo, name="editar_articulo"),
    path("eliminar/<int:pk>/", views.eliminar_articulo, name="eliminar_articulo"),
    # --- Apuntes ---
    path("subir_apunte/", views.subir_apunte, name="subir_apunte"),
    # ESTO DEBE ESTAR SÍ O SÍ para que el index funcione:
    path("buscar/", views.buscar_apuntes, name="buscar_apuntes"),
]

from django.urls import path
from . import views

app_name = "blog_edicion"

urlpatterns = [
    # Cuando entres a /articulos/, mostraremos todas las noticias en lugar del home
    path("", views.ver_todas_noticias, name="ver_todas_noticias"),
    # Tus funciones de Blog
    path("crear/", views.crear_articulo, name="crear_articulo"),
    path("detalle/<int:pk>/", views.articulo_detalle, name="articulo_detalle"),
    path("editar/<int:pk>/", views.editar_articulo, name="editar_articulo"),
    path("eliminar/<int:pk>/", views.eliminar_articulo, name="eliminar_articulo"),
    path("todas/", views.ver_todas_noticias, name="ver_todas_noticias"),
    # La nueva función para APUNTES
    path("subir_apunte/", views.subir_apunte, name="subir_apunte"),
]

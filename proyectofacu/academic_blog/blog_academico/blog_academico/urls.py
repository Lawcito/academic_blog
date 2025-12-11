from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importamos la vista del home corregida
from blog_academico import views as views_home

urlpatterns = [
    path("admin/", admin.site.urls),
    # El Home del sitio
    path("", views_home.home, name="home"),
    # Registro de usuarios
    path("registro/", views_home.registro, name="registro"),
    # Login/Logout (Django ya trae esto hecho)
    path("accounts/", include("django.contrib.auth.urls")),
    # Las URLs de tu aplicación (Noticias, Apuntes, etc.)
    path("articulos/", include("blog_edicion.urls")),
]

# ESTO ES LO IMPORTANTE:
# Le dice a Django: "Si estás en modo DEBUG, mostrá las imágenes y PDFs que están en MEDIA"
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

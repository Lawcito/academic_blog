from django.contrib import admin
from django.urls import path, include
from blog_academico import views

# Importamos las configuraciones de Django para servir archivos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # RUTA PRINCIPAL DE LA APLICACIÓN (Inicio)
    path("", views.home, name="home"),
    # RUTAS DE AUTENTICACIÓN (Soluciona el error 'logout')
    path("accounts/", include("django.contrib.auth.urls")),
    # RUTAS DE LA APLICACIÓN 'blog_edicion'
    path("articulos/", include("blog_edicion.urls")),
]

# =========================================================
# CONFIGURACIÓN CRÍTICA PARA ARCHIVOS MULTIMEDIA Y VIDEO
# =========================================================
if settings.DEBUG:
    # Servir archivos subidos (MEDIA_URL, para flyers y apuntes)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Servir archivos estáticos (STATIC_URL, para el video de fondo, CSS, JS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views

app_name = 'blog_edicion'

urlpatterns = [
    path('', views.home, name='lista_articulos'),
    path('<int:pk>/', views.articulo_detalle, name='articulo_detalle'),
    path('categoria/<int:pk>/', views.articulos_por_categoria, name='articulos_por_categoria'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),
]

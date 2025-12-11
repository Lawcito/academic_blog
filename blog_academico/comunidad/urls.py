# comunidad/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('apuntes/', views.apuntes_lista, name='apuntes_lista'),
    path('apuntes/nuevo/', views.apunte_nuevo, name='apunte_nuevo'),

    path('materiales/', views.materiales_lista, name='materiales_lista'),
    path('materiales/nuevo/', views.material_nuevo, name='material_nuevo'),

    path('debates/', views.debates_lista, name='debates_lista'),

    # 👇 ESTA ES LA LÍNEA IMPORTANTE PARA QUE FUNCIONE TU ENLACE
    path('debates/nuevo/', views.debate_nuevo, name='debate_nuevo'),

    path('debates/<int:pk>/', views.debate_detalle, name='debate_detalle'),
]




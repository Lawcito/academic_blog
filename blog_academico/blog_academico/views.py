# Archivo: blog_academico/blog_academico/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

# CORRECCIÓN: Importamos los modelos nuevos (Sin Categoria)
from blog_edicion.models import Articulo, Apunte, Evento


def home(request):
    # 1. Calendario (Izquierda) - Próximos eventos
    eventos = Evento.objects.filter(fecha__gte=timezone.now()).order_by("fecha")[:5]

    # 2. Noticias (Centro) - Ordenadas por fecha
    articulos = Articulo.objects.all().order_by("-fecha_publicacion")

    # 3. Apuntes (Derecha) - Últimos subidos
    apuntes = Apunte.objects.all().order_by("-fecha_subida")[:5]

    context = {"eventos": eventos, "articulos": articulos, "apuntes": apuntes}
    return render(request, "index.html", context)


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {"form": form})

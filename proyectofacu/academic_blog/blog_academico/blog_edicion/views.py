# Archivo: blog_edicion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Importamos modelos nuevos
from .models import Articulo, Apunte

# Importamos los formularios (asegúrate de tenerlos en forms.py)
from .forms import ArticuloForm, ApunteForm

# --- TUS FUNCIONES DE BLOG (LO QUE YA TENÍAS) ---


@login_required
def crear_articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect("home")  # Redirige al home del proyecto
    else:
        form = ArticuloForm()
    return render(request, "blog_edicion/crear_articulo.html", {"form": form})


@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    # Seguridad: solo el autor edita
    if articulo.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este artículo.")

    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ArticuloForm(instance=articulo)
    return render(
        request,
        "blog_edicion/editar_articulo.html",
        {"form": form, "articulo": articulo},
    )


@login_required
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        return HttpResponseForbidden("No tienes permiso.")
    articulo.delete()
    return redirect("home")


def articulo_detalle(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, "blog_edicion/articulo_detalle.html", {"articulo": articulo})


def ver_todas_noticias(request):
    articulos = Articulo.objects.all().order_by("-fecha_publicacion")
    return render(request, "blog_edicion/todas_noticias.html", {"articulos": articulos})


# --- LO NUEVO: SUBIR APUNTES ---


@login_required
def subir_apunte(request):
    if request.method == "POST":
        form = ApunteForm(request.POST, request.FILES)
        if form.is_valid():
            apunte = form.save(commit=False)
            apunte.autor = request.user
            apunte.save()
            return redirect("home")
    else:
        form = ApunteForm()
    return render(request, "blog_edicion/subir_apunte.html", {"form": form})

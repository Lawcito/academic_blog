from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Articulo, Apunte, Materia, Carrera
from .forms import ArticuloForm, ApunteForm

# --- SECCIÓN NOTICIAS ---


@login_required
def crear_articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            # Sugerencia: Si quieres volver a la lista de noticias en vez del home,
            # cambia "home" por el nombre de tu url de noticias.
            return redirect("home")
    else:
        form = ArticuloForm()
    return render(request, "blog_edicion/crear_articulo.html", {"form": form})


@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        return HttpResponseForbidden("No tienes permiso.")

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
    # Trae las noticias de la más nueva a la más vieja
    articulos = Articulo.objects.all().order_by("-fecha_publicacion")
    return render(request, "blog_edicion/todas_noticias.html", {"articulos": articulos})


# --- SECCIÓN APUNTES ---


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


# --- BUSCADOR ---


def buscar_apuntes(request):
    # 1. Empezamos trayendo TODOS los apuntes
    apuntes = Apunte.objects.all()

    # 2. Obtenemos los datos del filtro desde la URL
    q = request.GET.get("q")
    materia_id = request.GET.get("materia")
    carrera_id = request.GET.get("carrera")

    # 3. Aplicamos filtros solo si hay datos reales

    # Filtro por palabra clave (título)
    if q:
        apuntes = apuntes.filter(titulo__icontains=q)

    # Filtro por Materia
    if materia_id and materia_id != "":
        apuntes = apuntes.filter(materia_id=materia_id)

    # Filtro por Carrera
    if carrera_id and carrera_id != "":
        # Asume que el modelo Materia tiene una relación con Carrera
        apuntes = apuntes.filter(materia__carrera_id=carrera_id)

    # 4. Cargamos las listas para los desplegables del formulario de búsqueda
    materias = Materia.objects.all()
    carreras = Carrera.objects.all()

    context = {"apuntes": apuntes, "materias": materias, "carreras": carreras}
    return render(request, "blog_edicion/buscar_apuntes.html", context)

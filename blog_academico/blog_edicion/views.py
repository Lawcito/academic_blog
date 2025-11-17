from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo, Categoria
from .forms import ArticuloForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect('blog_edicion:articulo_detalle', pk=articulo.pk)
    else:
        form = ArticuloForm()
    return render(request, 'blog_edicion/crear_articulo.html', {'form': form})

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este artículo.")

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('blog_edicion:articulo_detalle', pk=articulo.pk)
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'blog_edicion/editar_articulo.html', {'form': form, 'articulo': articulo})

def home(request):
    articulos = Articulo.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "index.html", {'articulos': articulos, 'categorias': categorias})

def articulo_detalle(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'articulo_detalle.html', {'articulo': articulo})

def articulos_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    articulos = Articulo.objects.filter(categoria=categoria)
    return render(request, 'articulos_por_categoria.html', {'categoria': categoria, 'articulos': articulos})
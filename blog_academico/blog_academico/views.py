from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from blog_edicion.models import Articulo, Categoria

# 👉 NUEVO: import de la app de comunidad
from comunidad.models import Apunte, MaterialEstudio, Debate


def home(request):
    articulos = Articulo.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "index.html", {'articulos': articulos, 'categorias': categorias})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    # Nuevo: traer datos reales para el panel derecho
    ultimos_apuntes = Apunte.objects.order_by('-fecha')[:3]
    ultimos_materiales = MaterialEstudio.objects.order_by('-fecha')[:3]
    ultimos_debates = Debate.objects.order_by('-fecha')[:3]

    return render(
        request,
        'registration/registro.html',
        {
            'form': form,
            'ultimos_apuntes': ultimos_apuntes,
            'ultimos_materiales': ultimos_materiales,
            'ultimos_debates': ultimos_debates,
        }
    )
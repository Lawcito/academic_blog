from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from blog_edicion.models import Articulo, Categoria

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
    return render(request, 'registration/registro.html', {'form': form})

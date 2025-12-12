from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Apunte, MaterialEstudio, Debate, MensajeDebate
from .forms import ApunteForm, MaterialEstudioForm, DebateForm, MensajeDebateForm


# --- APUNTES ---

def apuntes_lista(request):
    apuntes = Apunte.objects.select_related('usuario').order_by('-fecha')
    return render(request, 'comunidad/apuntes.html', {'apuntes': apuntes})


@login_required
def apunte_nuevo(request):
    if request.method == 'POST':
        form = ApunteForm(request.POST)
        if form.is_valid():
            apunte = form.save(commit=False)
            apunte.usuario = request.user
            apunte.save()
            return redirect('apuntes_lista')
    else:
        form = ApunteForm()
    return render(request, 'comunidad/apunte_form.html', {'form': form})


# --- MATERIAL DE ESTUDIO ---

def materiales_lista(request):
    materiales = MaterialEstudio.objects.order_by('-fecha')
    return render(request, 'comunidad/materiales.html', {'materiales': materiales})


@login_required
def material_nuevo(request):
    if request.method == 'POST':
        form = MaterialEstudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('materiales_lista')
    else:
        form = MaterialEstudioForm()
    return render(request, 'comunidad/material_form.html', {'form': form})


# --- DEBATES ---

def debates_lista(request):
    debates = Debate.objects.select_related('creado_por').order_by('-fecha')
    return render(request, 'comunidad/debates.html', {'debates': debates})


@login_required
def debate_nuevo(request):
    if request.method == 'POST':
        form = DebateForm(request.POST)
        if form.is_valid():
            debate = form.save(commit=False)
            debate.creado_por = request.user
            debate.save()
            return redirect('debates_lista')
    else:
        form = DebateForm()
    return render(request, 'comunidad/debate_form.html', {'form': form})


@login_required
def debate_detalle(request, pk):
    debate = get_object_or_404(Debate, pk=pk)
    mensajes = debate.mensajes.select_related('autor')

    if request.method == 'POST':
        form = MensajeDebateForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.debate = debate
            mensaje.autor = request.user
            mensaje.save()
            return redirect('debate_detalle', pk=pk)
    else:
        form = MensajeDebateForm()

    contexto = {
        'debate': debate,
        'mensajes': mensajes,
        'form': form,
    }
    return render(request, 'comunidad/debate_detalle.html', contexto)

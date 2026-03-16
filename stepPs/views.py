from django.shortcuts import render, get_object_or_404,redirect
from .models import Perfil, Vaga, Candidatura
from .forms import CandidaturaForm
from django.contrib.auth.decorators import login_required

def home(request):

    vagas = Vaga.objects.all()[:3]

    return render(request, 'home.html', {'vagas': vagas})

def lista_vagas(request):

    vagas = Vaga.objects.all()

    return render(request, 'vagas.html', {'vagas': vagas})

def detalhes_vaga(request, vaga_id):

    vaga = get_object_or_404(Vaga, id=vaga_id)
    
    return render(request, 'detalhes_vaga.html', {'vaga': vaga})

@login_required
def candidatar(request, vaga_id):

    vaga = get_object_or_404(Vaga, id=vaga_id)
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':

        Candidatura.objects.get_or_create(
            usuario=perfil,
            vaga=vaga,
        )

        return redirect('lista_vagas')
    
    return render(request, 'candidatar.html', {'vaga': vaga})

@login_required
def minhas_candidaturas(request):

    perfil, created = Perfil.objects.get_or_create(user=request.user)
    candidaturas = Candidatura.objects.filter(usuario=perfil)

    return render(request, 'minhas_candidaturas.html', {'candidaturas': candidaturas})
from django.shortcuts import render, redirect
from .models import Inscricao
from django.contrib import messages

def home(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        if Inscricao.objects.filter(email=email).exists():
            messages.error(request, 'Este email já foi cadastrado.')
            return redirect('inscricao')

        plataformas = request.POST.getlist('plataformas')
        plataformas_str = ', '.join(plataformas)

        Inscricao.objects.create(
            nome = request.POST.get('nome'),

            email = email,

            pergunta1 = request.POST.get('pergunta1'),
            pergunta2 = request.POST.get('pergunta2'),
            pergunta3 = request.POST.get('pergunta3'),
            nicknames = request.POST.get('nicknames'),
            plataformas = plataformas_str,
        )
            
        

        messages.success(request, 'Inscrição enviada com sucesso!')
        return redirect('inscricao')  

    return render(request, 'home.html')


def como_funciona(request):
    return render(request, 'como_funciona.html')
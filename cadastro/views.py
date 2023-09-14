from django.shortcuts import render
from django.http import HttpResponse
from .models import CadastrarUsuario

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        cadastrarUsuario = CadastrarUsuario(nome=nome, sobrenome=sobrenome, data_nascimento=data_nascimento, email=email, senha=senha)
        cadastrarUsuario.save()
        return HttpResponse('Usuário cadastrado com sucesso!')

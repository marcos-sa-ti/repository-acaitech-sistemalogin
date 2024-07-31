from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Criando uma funcao
def index(request):
    #Primeiro parametro sempre é a requisicao
    return render (request, 'home.html')

def exibirTelaCadastroFuncionario(request):
    return render(request,'cadastro.html')


def exibirTelaImagem(request):
    return render(request, 'imagem.html')

def exibirTelaLoginAcaiTech(request):
    return render(request, 'login.html')
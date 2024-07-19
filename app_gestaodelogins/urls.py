from django.urls import path

# Importando a funcao para exibir a pagina index (home)
from app_gestaodelogins.views import index 
# Importando a funcao para exibir a pagina para o cadastro de funcionario (home)
from app_gestaodelogins.views import exibirTelaCadastroFuncionario 

from app_gestaodelogins.views import exibirTelaImagem

#Urls que vamos atender nessa aplicacao

#Lista de endpoints da aplicacao

urlpatterns = [
    # Chama a funcao index criada no arquivo .views
    path('',index),
    path('cadastro/',exibirTelaCadastroFuncionario),
    path('exibirimagem/',exibirTelaImagem)
]

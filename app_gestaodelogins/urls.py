from django.urls import path

# Importando a funcao para exibir a pagina index (home)
from app_gestaodelogins.views import index 
# Importando a funcao para exibir a pagina para o cadastro de funcionario (home)
from app_gestaodelogins.views import exibirTelaCadastroFuncionario 
# Importando a funcao para exibir a pagina de exibicao de imagem
from app_gestaodelogins.views import exibirTelaImagem
# Importando a funcao para exibir a tela de login da acai tech
from app_gestaodelogins.views import exibirTelaLoginAcaiTech

#Urls que vamos atender nessa aplicacao

#Lista de endpoints da aplicacao

urlpatterns = [
    # Chama a funcao index criada no arquivo .views
    path('',index, name='index'),
    path('cadastro/',exibirTelaCadastroFuncionario),
    # Name = Nome do parametro para chamarmos dentro da pagina home
    path('exibirimagem/', exibirTelaImagem, name='imagem'),
    path('acaitech/login',exibirTelaLoginAcaiTech)
]

from django.contrib import admin
from django.urls import path
from django.urls import include

# Importando a funcao para exibir a pagina index (home)
from app_gestaodelogins.views import index 
#Urls que vamos atender nessa aplicacao

urlpatterns = [
    path('admin/', admin.site.urls),
    # Chama as urls do aplicativo.
    path('',include('app_gestaodelogins.urls'))
]

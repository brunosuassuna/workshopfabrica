# Configuração das URLs da aplicação 'api_rest'
from django.contrib import admin
from django.urls import path, include

# Importa as views (funções de visualização) da aplicação
from . import views

urlpatterns = [
    # Define a URL raiz como a função 'get_users' da aplicação com o nome 'get_all_users'
    path('', views.get_users, name='get_all_users'),
    # Define uma URL que aceita um parâmetro 'nick' como parte da URL, usando a função 'get_by_nick'
    path('user/<str:nick>', views.get_by_nick), 
    # Define uma URL chamada 'data' que mapeia para a função 'user_manager' 
    path('data', views.user_manager),
]

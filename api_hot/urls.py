# Configuração das URLs da aplicação Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
# URL de administração do Django
    path('admin/', admin.site.urls),
    # Inclui as URLs da aplicação 'api_rest' com um nome 'api_rest_urls'
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
]

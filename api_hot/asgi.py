"""
ASGI config for api_hot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

i# Importa o módulo (os) para lidar com variáveis de ambiente
import os

# Importa a função (get_asgi_application) do Django para obter a aplicação ASGI
from django.core.asgi import get_asgi_application

# Define a configuração do ambiente do Django usando o arquivo de configurações (api_hot.settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_hot.settings')

# Obtém a aplicação ASGI do Django
application = get_asgi_application()
"""
WSGI config for api_hot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Importa o módulo 'os' para lidar com variáveis de ambiente
import os

# Importa a função 'get_wsgi_application' do Django para obter a aplicação WSGI
from django.core.wsgi import get_wsgi_application

# Define a configuração do ambiente do Django usando o arquivo de configurações 'api_hot.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_hot.settings')

# Obtém a aplicação WSGI do Django
application = get_wsgi_application()




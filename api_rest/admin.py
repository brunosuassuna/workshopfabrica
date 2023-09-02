# Importa o módulo 'admin' do Django
from django.contrib import admin

# Importa o modelo 'User' definido na aplicação atual
from .models import User

# Registra o modelo 'User' no painel de administração do Django
admin.site.register(User)


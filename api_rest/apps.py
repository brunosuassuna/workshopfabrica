# Importa a classe AppConfig do Django
from django.apps import AppConfig

# Define a classe 'ApiRestConfig' que herda de 'AppConfig'
class ApiRestConfig(AppConfig):
    # Esta classe é usada para configurar a aplicação 'api_rest'.

    # Define o campo 'default_auto_field' para especificar o tipo de campo automático para chaves primárias.
    # Neste caso, usa 'django.db.models.BigAutoField'.
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o campo 'name' para especificar o nome da aplicação, que é 'api_rest'.
    name = 'api_rest'


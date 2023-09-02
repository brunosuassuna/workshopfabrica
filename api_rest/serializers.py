# Importa o módulo serializers do Django REST framework
from rest_framework import serializers

# Importa o modelo 'User' que será serializado
from .models import User

# Define a classe 'UserSerializer' que herda de 'serializers.ModelSerializer'
class UserSerializer(serializers.ModelSerializer):
    # A classe 'UserSerializer' é usada para serializar/desserializar instâncias do modelo 'User'.

    class Meta:
        # Define a metaclasse 'Meta' para configurar o serializador
        model = User  # Define o modelo que será serializado como 'User'
        fields = '__all__'  # Inclui todos os campos do modelo no serializador




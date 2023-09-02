# Importa o módulo models do Django
from django.db import models

# Define a classe do modelo 'User'
class User(models.Model):
    
    # Define o campo 'user_nickname' como chave primária (primary_key=True),
    # limitado a 100 caracteres (max_length=100) e com valor padrão vazio ('')
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')

    # Define o campo 'user_name' como um campo de texto com um limite máximo de 150 caracteres (max_length=150)
    # e com valor padrão vazio ('')
    user_name = models.CharField(max_length=150, default='')

    # Define o campo 'user_email' como um campo de endereço de e-mail válido (EmailField)
    # com valor padrão vazio ('')
    user_email = models.EmailField(default='')

    # Define o campo 'user_age' como um campo de número inteiro (IntegerField) com valor padrão 0
    user_age = models.IntegerField(default=0)

    # Define o método '__str__' para representar uma instância 'User' como uma string personalizada
    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
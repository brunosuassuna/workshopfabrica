#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Importa os módulos e bibliotecas necessários
import os
import sys

# Define a função principal 'main'
def main():
    """Run administrative tasks."""

    # Define a configuração do ambiente do Django usando o arquivo 'api_hot.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_hot.settings')

    try:
        # Tenta importar a função 'execute_from_command_line' do Django para executar comandos
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Se houver um erro de importação, levanta uma exceção informativa
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Executa o comando da linha de comando do Django com os argumentos do sistema
    execute_from_command_line(sys.argv)

# Executa a função 'main' se este arquivo for o ponto de entrada do programa
if __name__ == '__main__':
    main()
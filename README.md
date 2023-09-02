# workshopfabrica

# Projeto - API de Gerenciamento de Usuários

Este é um projeto que demonstra uma API de gerenciamento de usuários construída com o framework Django e o Django REST framework. A API permite realizar operações CRUD (Criar, Ler, Atualizar e Excluir) em registros de usuários, como apelido (nickname), nome, e-mail e idade.

## Funcionalidades Principais

- Listar Todos os Usuários: Recupere uma lista de todos os usuários cadastrados na API.

- Obter Usuário por Apelido: Recupere informações de um usuário específico com base em seu apelido (nickname).

- Criar Novo Usuário: Adicione um novo usuário à base de dados fornecendo informações como apelido, nome, e-mail e idade.

- Atualizar Usuário: Atualize informações de um usuário existente, incluindo apelido, nome, e-mail e idade.

- Excluir Usuário: Remova um usuário da base de dados com base em seu apelido.

## Configuração do Projeto

- O projeto usa o Django como framework web e o Django REST framework para criar uma API RESTful.
- O modelo de dados `User` é definido para armazenar informações de usuário na base de dados.
- As URLs da API são configuradas para mapear para funções de visualização que realizam operações CRUD nos registros de usuário.
- Um serializador é utilizado para converter objetos `User` em formato JSON para comunicação com a API.
- O projeto inclui configurações para rodar em servidores ASGI ou WSGI, como Daphne, Uvicorn, Gunicorn ou mod_wsgi.

## Requisitos

Para executar o projeto em seu ambiente local, você precisa ter o Python e o Django instalados. Além disso, é recomendável criar e ativar um ambiente virtual para gerenciar as dependências do projeto.

```bash
# Crie um ambiente virtual (opcional)
python -m venv myenv

# Ative o ambiente virtual
source myenv/bin/activate

# Instale as dependências
pip install -r requirements.txt

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

# Endpoint para obter todos os usuários (GET)
@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Endpoint para obter ou atualizar um usuário pelo apelido (nick) (GET e PUT)
@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(user_nickname=nick)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Endpoint que lida com todas as operações CRUD para usuários (GET, POST, PUT, DELETE)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    # Obter um usuário pelo apelido (nick) (GET)
    if request.method == 'GET':
        try:
            user_nickname = request.GET.get('user')
            if user_nickname is not None:
                try:
                    user = User.objects.get(user_nickname=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Criar um novo usuário (POST)
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Atualizar um usuário pelo apelido (nick) (PUT)
    if request.method == 'PUT':
        nickname = request.data['user_nickname']
        try:
            updated_user = User.objects.get(user_nickname=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Excluir um usuário pelo apelido (nick) (DELETE)
    if request.method == 'DELETE':
        try:
            user_nickname = request.data.get('user_nickname')
            user_to_delete = User.objects.get(user_nickname=user_nickname)
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
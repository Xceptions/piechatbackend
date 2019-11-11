from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import status
from .models import Chats
from .serializers import UserSerializer, ChatSerializer

UserModel = get_user_model()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        validated_data = request.data
        user = UserModel.objects.create(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        # token = Token.objects.create(user=settings.AUTH_USER_MODEL)
        serialize = UserSerializer(user, context={'request': request})
        data = serialize.data
        token = Token.objects.get(user=user).key
        data['token'] = token
        return Response(data)


## to login, username=email, password is password
## login view already implemented by django-rest-framework


def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...

class ChatsView(APIView):
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return redirect('%s?next%s' % (settings.LOGIN_URL, request.path))
        getchat = Chats.objects.all()
        serializer = ChatSerializer(getchat, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if not request.user.is_authenticated:
            return redirect('%s?next%s' % (settings.LOGIN_URL, request.path))
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk):
    #     getbuild = Builds.objects.get(pk=pk)
    #     serializer = BuildsSerializer(getbuild, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     getbuild = Builds.objects.get(pk=pk)
    #     getbuild.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    ## after you have been authorized: http http://127.0.0.1:8000/chats/  'Authorization: Token faa3eac44321d6d0ac425339093965c83d7599c1'

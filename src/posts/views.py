from django.shortcuts import render
from .serializers import Post, PostSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
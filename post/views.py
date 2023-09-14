from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Post, Comment, Rating
from .serializers import PostSerializer

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


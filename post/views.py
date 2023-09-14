from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from .models import Post, Comment, Rating
from .serializer import

class Post(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class =
    permission_classes = []

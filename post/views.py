from datetime import datetime

from django.contrib.sites import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.response import Response

from .models import Post, Comment, Rating
from .permissions import Permissions
from .serializers import PostSerializer, CommentSerializer, RatingSerializer


class PostListCreateApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [Permissions]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListCreateApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            serializer.save(author=None)
        else:
            serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [Permissions]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RatingListCreateApiView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [Permissions]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RatingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [Permissions]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

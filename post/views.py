from datetime import datetime

from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, request
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
        if serializer.is_valid():
            def telegram_bot_sendtext(bot_message):
                bot_token = '6009637428:AAFc_6QOklxowo6JymlAARKTRreFkxOZqQc'
                bot_chatID = '912402374'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

                response = requests.get(send_text)
                response.json()

                post_title = serializer.validated_data.get('title')
                post_text = serializer.validated_data.get('text')
                post_created = datetime.today().strftime('%Y-%m-%d %H:%M')
                telegram_bot_sendtext(
                bot_message=f"Пост с названием {post_title} с текстом {post_text} успешно создан {post_created}")
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        serializer.save(user=self.request.user)


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

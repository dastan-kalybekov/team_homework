from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from .models import User
from .serializer import
class UserListCreateApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

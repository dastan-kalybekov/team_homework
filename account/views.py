from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(http_method_names=['GET', 'POST'])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes([IsAdminUser, AllowAny])
def user_list_api_view(request):
    if request.method == 'GET' and request.user.is_staff:
        users = User.objects.all()
        serializer = UserSerializer(data=users, many=True)
        serializer.is_valid()
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

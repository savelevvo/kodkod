from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from .serializers import AuthUserSerializer
from .models import AuthUser


class AuthUserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk, format=None):
        user = get_object_or_404(AuthUser, pk=pk)
        serializer = AuthUserSerializer(user)
        return Response(serializer.data)


class AuthUserRegister(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username, password = request.POST.get('username', ''), request.POST.get('password', '')
        if not username or not password:
            return Response({'error': 'both username and password must be provided'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = AuthUser.objects.create(username=username)
            user.set_password(password)
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AuthUserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if request.auth:
            return Response({'error': 'Already logged in'}, status=status.HTTP_400_BAD_REQUEST)
        username, password = request.POST.get('username', ''), request.POST.get('password', '')
        if not username or not password:
            return Response({'error': 'both username and password must be provided'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AuthUserLogout(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

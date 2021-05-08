from django.shortcuts import render
from django.conf import settings
from django.contrib import auth

from rest_framework.generics import GenericAPIView
from rest_framework import response, status
import jwt

from authentication.serializers import RegisterSerializer, LoginSerializer, UserSerializer



class RegisterAPIView(GenericAPIView):
    
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(
            email=email, password=password)
        
        if user:
            auth_token = jwt.encode({'email': user.email}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)
            data = {
                'user': serializer.data,
                'token': auth_token,
                }
            return response.Response(data, status=status.HTTP_200_OK)
        

        return response.Response({
            'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

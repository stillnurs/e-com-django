from django.shortcuts import render
from django.conf import settings

from rest_framework.generics import GenericAPIView
from rest_framework import response, status, permissions
import jwt

from authentication.serializers import *
from .renderer import UserRenderer



class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        
        return response.Response(user_data, status=status.HTTP_201_CREATED)
        


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
                
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return response.Response(serializer.data, status=status.HTTP_200_OK)



class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
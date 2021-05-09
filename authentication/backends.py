from django.conf import settings

from rest_framework import authentication, exceptions
import jwt

from .models import User


class JWTAuthentication(authentication.BasicAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        
        prefix, token = auth_data.decode('utf-8').split(' ')
        
        if User.object.get(is_vendor):
            user_status = 'vendor'
        user_status = 'client'

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms="HS256")
            user_email = User.objects.get(email=payload['email'])
            return (user_email, user_status, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid, login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired, login')
        
        
        return super().authenticate(request)
from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView, )
from authentication import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),

    # path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('request-reset-email/', RequestPasswordResetEmail.as_view(),
    #      name="request-reset-email"),
    # path('password-reset/<uidb64>/<token>/',
    #      PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete', SetNewPasswordAPIView.as_view(),
    #      name='password-reset-complete')

]

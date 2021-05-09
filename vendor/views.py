from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Stock
from .serializers import *

from authentication.views import RegisterAPIView, LoginAPIView



class VendorRegisterView(RegisterAPIView):
    serializer_class = VendorRegisterSerializer



class VendorLoginView(LoginAPIView):
    serializer_class = VendorLoginSerializer



class StockListAPIView(ListCreateAPIView):

    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Stock.objects.filter(owner=self.request.user)



class StockDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'

    def get_queryset(self):
        return Stock.objects.filter(owner=self.request.user)

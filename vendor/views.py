from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, viewsets, response, status
from rest_framework.decorators import action

from .models import Stock
from .serializers import *



class VendorDashboardAPIView(viewsets.ModelViewSet):
    pass

class StockListAPIView(ListCreateAPIView):

    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except ValueError as e:
            return response.Response(e, status=status.HTTP_401_UNAUTHORIZED)
    def get_queryset(self):
        # try:
        #     return Stock.objects.filter(owner=self.request.user)
        # except ValueError as e:
        #     return response.Response("You are not authorized to open this page", status=status.HTTP_401_UNAUTHORIZED)
        return Stock.objects.filter(owner=self.request.user)
        


class StockDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'

    def get_queryset(self):
        return Stock.objects.filter(owner=self.request.user)

# from django.shortcuts import get_object_or_404

# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# from .serializers import *
# from .models import *


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializers = UserRoleSerializer(queryset, many=True)
#     permission_classes = (IsAuthenticated,)



# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializers = StoreSerializer(queryset, many=True)
    



# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializers = CategorySerializer(queryset, many=True)




# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializers = ProductSerializer(queryset, many=True)

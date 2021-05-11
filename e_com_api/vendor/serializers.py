from rest_framework import serializers

from .models import Vendor, Stock
from authentication.serializers import UserSerializer



class VendorSerializer(UserSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'



class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('id', 'title', 'country', 'photo', 'count')
        lookup_field = 'id'


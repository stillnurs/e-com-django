# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

# from .models import *



# class StoreSerializer(serializers.ModelSerializer):

#     title = serializers.CharField(max_lenght=255, required=True)
#     owner = UserSerializer(required=True, many=True)


#     # def create(self, st):
#     #     store = Product.objects.create_object(
#     #         st['title']=self.title,
#     #         st['store']=self.owner,
#     #         )

#     #     return store


#     class Meta:
#         model = Store
#         fields = '__all__'



# class CategorySerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=255, required=True)
#     store = StoreSerializer(required=False, many=True,)


#     # def create(self, cat):
#     #     category = Product.objects.create_object(
#     #         cat['title']=self.title,
#     #         cat['store']=self.store,
#     #         )

#     #     return category
    

#     class Meta:
#         model = Category
#         fields = '__all__'



# class ProductSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=255, required=True)
#     image = serializers.ImageField(user_url = True, blank=True, allow_null=True)
#     price = serializers.FloatField(required=True)
#     category = CategorySerializer(required=False, many=True)
    
    
#     # def create(self, prod):
#     #     product = Product.objects.create_object(
#     #         prod['title']=self.title,
#     #         prod['image']=self.image,
#     #         prod['price']=self.price,
#     #         prod['category']=self.category
#     #         )

#     #     return product


#     class Meta:
#         model = Product
#         fields = '__all__'

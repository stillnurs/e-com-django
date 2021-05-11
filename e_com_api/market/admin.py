from django.contrib import admin

from market.models import Category, Product

admin.site.register(Product)
admin.site.register(Category)
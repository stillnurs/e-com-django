from django.db import models
from django.conf import settings



User = settings.AUTH_USER_MODEL



class Store(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
        


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    store = models.ForeignKey(Store, related_name='store', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']


    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    

    class Meta:
        ordering = ['-title']

    
    def __str__(self):
        return self.title

    
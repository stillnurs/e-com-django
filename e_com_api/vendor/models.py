from django.db import models
from authentication.models import User



class Vendor(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, null=False, blank=False, db_index=True)
    phone = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        ordering = ['store_name']

    def __str__(self):
        return self.store_name
    


class Stock(models.Model):
    owner = models.ForeignKey(to=Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(verbose_name='photo')
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    


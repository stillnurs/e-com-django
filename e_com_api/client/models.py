from django.db import models
from authentication.models import User



class Client(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.store_name
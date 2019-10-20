from django.db import models

# Create your models here.


class Arduino(models.Model):

    name = models.CharField(max_length=5)
    data = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
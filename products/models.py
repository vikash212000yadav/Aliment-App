from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, blank=False)
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

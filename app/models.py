from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    popular = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

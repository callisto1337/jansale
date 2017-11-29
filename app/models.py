from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, blank=True)
    popular = models.BooleanField()
    new = models.BooleanField()

    def __str__(self):
        return self.name

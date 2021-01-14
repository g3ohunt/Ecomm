from django.db import models

# Create your models here.


class Products(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    price = models.FloatField()
    discountPrice = models.FloatField()
    category = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.CharField(max_length=5000)


class Order(models.Model):

    items = models.TextField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
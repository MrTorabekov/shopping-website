from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ...


class Home(models.Model):
    product_Theme = models.CharField(max_length=100)
    product_name = models.CharField(max_length=120)
    text = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    text = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')


class About(models.Model):
    name = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images')


class contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

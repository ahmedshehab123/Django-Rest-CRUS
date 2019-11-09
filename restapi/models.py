from django.db import models


# Create your models here.

class Products(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=800)




class News(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=2000)


class Users(models.Model):
    id = models.IntegerField
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=2000)


class adds(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=250)
    value = models.CharField(max_length=2000)


def __str__(self):
    return self.name

from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    toppings = models.ManyToManyField(Topping)
    price = models.FloatField(max_length=5)

    def __str__(self):
        return self.name
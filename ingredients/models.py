from django.db import models

# Create your models here.
# cookbook/ingredients/models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )
    qty = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.category}"


class Chef(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=30)
    stars = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

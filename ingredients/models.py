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

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=30)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.name

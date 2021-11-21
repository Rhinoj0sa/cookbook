from django.contrib import admin

from django.contrib import admin
from ingredients.models import Category, Ingredient, Chef

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Chef)

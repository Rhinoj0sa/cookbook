# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")
        # exclude = ("id",)


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


# esto iria en schema.py
class Query(graphene.ObjectType):
    todos_los_ingredientes = graphene.List(IngredientType)
    categoria_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_todos_los_ingredientes(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.all()

    def resolve_categoria_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

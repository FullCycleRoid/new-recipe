from rest_framework import serializers
from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='recipe:tag-detail',
        lookup_field='name'
    )

    class Meta:
        model = Tag
        fields = ['id', 'pk', 'name', 'user', 'url']


class IngredientSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='recipe:ingredients-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Ingredient
        fields = ['id', 'pk', 'name', 'user', 'url']


class RecipeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='recipe:recipe-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Recipe
        fields = ['id', 'pk', 'name', 'cooking_time', 'price', 'tags', 'ingredients', 'url', 'user']


class RecipeImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'image']

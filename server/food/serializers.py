from rest_framework import serializers
from food.models import Food, FoodGroup, Recipe, RecipeFood

class FoodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodGroup
        fields=('__all__')

class FoodSerializer(serializers.ModelSerializer):
    food_group_id = serializers.IntegerField(write_only = True)
    food_group = FoodGroupSerializer(read_only = True)

    class Meta:
        model=Food
        fields=('__all__')

class RecipeSerializer(serializers.ModelSerializer):
    food_ids = serializers.ListField(child = serializers.IntegerField(), read_only = True)

    foods = FoodSerializer(many = True, read_only = True)
    
    class Meta:
        model=Recipe
        fields=('__all__')

class RecipeFoodSerializer(serializers.ModelSerializer):
    food_id = serializers.IntegerField(write_only = True)
    recipe_id = serializers.IntegerField(write_only = True)

    food = FoodSerializer(read_only = True)
    recipe = RecipeSerializer(read_only = True)

    class Meta:
        model=RecipeFood
        fields=('__all__')
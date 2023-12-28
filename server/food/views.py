from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from food.models import Food, FoodGroup, Recipe, RecipeFood
from food.serializers import FoodSerializer, FoodGroupSerializer, RecipeSerializer, RecipeFoodSerializer

@csrf_exempt
def foodApi(request, id=0):
    if request.method == 'GET':
        food = Food.objects.all()
        foodSerializer = FoodSerializer(food, many = True)
        return JsonResponse(foodSerializer.data, safe = False)
    
    elif request.method == 'POST':
        foodData = JSONParser().parse(request)
        foodSerializer = FoodSerializer(data = foodData)
        if foodSerializer.is_valid():
            foodSerializer.save()
            return JsonResponse(foodSerializer.data, safe = False)
        
    elif request.method == 'PUT':
        foodData = JSONParser().parse(request)
        food = Food.objects.get(id = foodData['id'])
        foodSerializer = FoodSerializer(food, data = foodData)
        if foodSerializer.is_valid():
            foodSerializer.save()
            return JsonResponse(foodSerializer.data, safe = False)
        
    elif request.method == 'DELETE':
        food = Food.objects.get(id = id)
        food.delete()
        return JsonResponse('Deleted Successfully', safe = False)
    

@csrf_exempt
def foodGroupApi(request, id=0):
    if request.method == 'GET':
        foodGroups = FoodGroup.objects.all()
        foodGroups_serializer = FoodGroupSerializer(foodGroups, many = True)
        return JsonResponse(foodGroups_serializer.data, safe = False)
    
    elif request.method == 'POST':
        foodGroupData = JSONParser().parse(request)
        foodGroups_serializer = FoodGroupSerializer(data = foodGroupData)
        if foodGroups_serializer.is_valid():
            foodGroups_serializer.save()
            return JsonResponse(foodGroups_serializer.data, safe = False)
        
    elif request.method == 'PUT':
        foodGroupData = JSONParser().parse(request)
        foodGroup = FoodGroup.objects.get(id = foodGroupData['id'])
        foodGroups_serializer = FoodGroupSerializer(foodGroup, data = foodGroupData)
        if foodGroups_serializer.is_valid():
            foodGroups_serializer.save()
            return JsonResponse(foodGroups_serializer.data, safe = False)
        
    elif request.method == 'DELETE':
        foodGroup = FoodGroup.objects.get(id = id)
        foodGroup.delete()
        return JsonResponse('Deleted Successfully', safe = False)
    
@csrf_exempt
def recipeApi(request, id=0):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipeSerializer = RecipeSerializer(recipes, many = True)
        return JsonResponse(recipeSerializer.data, safe = False)
    
    elif request.method == 'POST':
        recipeData = JSONParser().parse(request)
        recipeSerializer = RecipeSerializer(data = recipeData)
        if recipeSerializer.is_valid():
            recipeSerializer.save()
        recipe_foods = []
        for food_id in recipeData['food_ids']:
            recipe_foods.append({
                'recipe_id': recipeSerializer.data['id'],
                'food_id': food_id
            })
        recipe_food_serializer = RecipeFoodSerializer(data = recipe_foods, many = True)
        if recipe_food_serializer.is_valid():
            recipe_food_serializer.save()
        recipe = Recipe.objects.get(id = recipeSerializer.data['id'])
        recipeSerializer = RecipeSerializer(recipe, data = recipeData)
        if recipeSerializer.is_valid():
            return JsonResponse(recipeSerializer.data, safe = False)

    elif request.method == 'PUT':
        recipeData = JSONParser().parse(request)
        recipe = Recipe.objects.get(id = recipeData['id'])
        recipeSerializer = RecipeSerializer(recipe, data = recipeData)
        if recipeSerializer.is_valid():
            recipeSerializer.save()
        for food in recipeSerializer.data['foods']:
            if food['id'] not in recipeData['food_ids']:
                recipe_food = RecipeFood.objects.filter(recipe_id = recipeData['id'], food_id = food['id'])
                recipe_food.delete()
        for food_id in recipeData['food_ids']:
            if not RecipeFood.objects.filter(recipe_id = recipeData['id'], food_id = food_id).exists():
                recipe_food = {
                    'recipe_id': recipeData['id'],
                    'food_id': food_id
                }
                recipe_food_serializer = RecipeFoodSerializer(data = recipe_food)
                if recipe_food_serializer.is_valid():
                    recipe_food_serializer.save()
        
        recipe = Recipe.objects.get(id = recipeSerializer.data['id'])
        recipeSerializer = RecipeSerializer(recipe, data = recipeData)
        if recipeSerializer.is_valid():
            return JsonResponse(recipeSerializer.data, safe = False)
        
        return_recipe = Recipe.objects.get(id = recipeSerializer.data['id'])
        return_recipeSerializer = RecipeSerializer(return_recipe, data = return_recipe)
        if return_recipeSerializer.is_valid():
            return JsonResponse(return_recipeSerializer.data, safe = False)

    elif request.method == 'DELETE':
        recipe = Recipe.objects.get(id = id)
        recipe.delete()
        return JsonResponse('Deleted Successfully', safe = False)
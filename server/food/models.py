from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    food_group = models.ForeignKey('FoodGroup', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Food'


class FoodGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Food_Group'

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField('Food', through = 'RecipeFood')
    
    class Meta:
        managed = False
        db_table = 'Recipe'

class RecipeFood(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    food = models.ForeignKey('Food', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Recipe_Food'
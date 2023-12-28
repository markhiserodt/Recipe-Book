from django.urls import path
from food import views

urlpatterns = [
    path('api/foodGroup', views.foodGroupApi),
    path('api/foodGroup/<int:id>', views.foodGroupApi),
    path('api/food', views.foodApi),
    path('api/food/<int:id>', views.foodApi),
    path('api/recipe', views.recipeApi),
    path('api/recipe/<int:id>', views.recipeApi)
]
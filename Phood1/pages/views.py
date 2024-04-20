from django.shortcuts import render
from django.http import HttpResponse
from recipe.models import Recipe, RecipeIngredients, Ingredient

def homepage_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})

def specific_recipe_view(request, recipe_id, *args, **kwargs):
    context = {}
    # Get the recipe by its primary key (recipe ID)
    context['recipe'] = Recipe.objects.get(pk=recipe_id)
    # Obtain all ingredients from the recipe_ingredients info
    recipe_ingredients = RecipeIngredients.objects.filter(recipe_id=recipe_id)
    # For each recipe_ingredient obtain its name & create a tuple
    ingredients_info = []
    # Group ingredients info together
    for ing in recipe_ingredients:
        ingredients_info.append([Ingredient.objects.get(name=ing.ingredient_id).name, ing.qty, ing.unit])
    context['ing_info'] = ingredients_info
    return render(request, "pages/specific_recipe.html", context)

def allrecipes_view(request, *args, **kwargs):
    context = {}
    recipes = Recipe.objects.all()
    context['recipes'] = recipes

    return render(request, "pages/allrecipes.html", context)
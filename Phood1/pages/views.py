from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from recipe.models import Recipe

def homepage_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})

def specific_recipe_view(request, *args, **kwargs):
    context = {}
    return render(request, "pages/specific_recipe.html", context)

def allrecipes_view(request, *args, **kwargs):
    context = {}
    recipes = Recipe.objects.all()
    context['recipes'] = recipes

    return render(request, "pages/allrecipes.html", context)
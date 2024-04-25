from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from recipe.models import Recipe, RecipeIngredients, Ingredient, Instructions
from Forms.forms import RecipeForm

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

    # Get all steps increasing order
    context['recipe_steps'] = Instructions.objects.filter(rec_id=recipe_id).order_by('step_number')
    return render(request, "pages/specific_recipe.html", context)

def allrecipes_view(request, ingredient, *args, **kwargs):
    context = {}
    # recipes = Recipe.objects.all()
    # recipes = Recipe.objects.filter(recipe__ingredient__name__iexact="pasta")
    pasta_recipes = []
    recipe_ingredient_with_pasta = RecipeIngredients.objects.filter(ingredient_id__name__icontains=ingredient)
    for recing_pasta in recipe_ingredient_with_pasta:
        pasta_recipes.append(Recipe.objects.get(pk=recing_pasta.recipe_id.pk))
    context['recipes'] = pasta_recipes

    return render(request, "pages/allrecipes.html", context)

def add_recipe_view(request, *args, **kwargs):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # 1) create Recipe
            # recipe_obj = Recipe.objects.create(title=form.cleaned_data['title'], cuisine=form.cleaned_data['cuisine'], time=picture=form.cleaned_data['time'])
            # 2) create all Ingredients
             # for ingredient in ing_csv_file:
            #     i = Ingredient.objects.create(name=form.cleaned_data['ingredient'])
            #     list_of_ings.append(i)
            # 3) create RecipeIngredients
            # for recing in instr_csv_file:
            #     RecipeIngredient.objects.create(rec_id=recipe_obj, ingredient_id=list_of_ings[counter], qty=form.cleaned_data['ing_qty'], unit=form.cleaned_data['ing_unit'])
            

            return redirect(homepage_view)
        else:
            # print(form.errors())
            form = RecipeForm()
    
    context = {'form': form}
    return render(request, 'pages/add_recipe.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from recipe.models import Recipe, RecipeIngredients, Ingredient, Instructions
from Forms.forms import RecipeForm, IngredientFormSet

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

def add_recipe_view(request, form1_done, *args, **kwargs):
    context = {}
    form_recipe = RecipeForm()
    formset=IngredientFormSet(queryset=Ingredient.objects.none())

    if form1_done and add_recipe_view.form1counter < 1:
        if request.method == "POST":
            form_recipe = RecipeForm(request.POST)
            if form_recipe.is_valid():
                add_recipe_view.form1counter += 1
                print(form_recipe.cleaned_data)
                # 1) create Recipe
                # recipe_obj = Recipe.objects.create(title=form_recipe.cleaned_data['title'], cuisine=form_recipe.cleaned_data['cuisine'], time=picture=form_recipe.cleaned_data['time'])
                # 2) create all Ingredients
                # for ingredient in ing_csv_file:
                #     i = Ingredient.objects.create(name=form_recipe.cleaned_data['ingredient'])
                #     list_of_ings.append(i)
                # 3) create RecipeIngredients
                # for recing in instr_csv_file:
                #     RecipeIngredient.objects.create(rec_id=recipe_obj, ingredient_id=list_of_ings[counter], qty=form_recipe.cleaned_data['ing_qty'], unit=form_recipe.cleaned_data['ing_unit'])
                

            else:
                # print(form_recipe.errors())
                form_recipe = RecipeForm()
    
    else:
        if request.method == "POST":
            formset = IngredientFormSet(request.POST)
            if formset.is_valid():
                for ing in formset:
                    print(ing.cleaned_data)
                return redirect(homepage_view)
        else:
            formset = IngredientFormSet()
    

    context = {'form_recipe': form_recipe,
               'formset': formset,
               'form1_done': form1_done}
    return render(request, 'pages/add_recipe.html', context)
add_recipe_view.form1counter=0

def ing_fset_view(request, *args, **kwargs):
    context = {}
    formset=IngredientFormSet(queryset=Ingredient.objects.none())
    if request.method == "POST":
        formset = IngredientFormSet(request.POST)
        if formset.is_valid():
            print(formset.cleaned_data)
        else:
            # print(form.errors())
            formset = IngredientFormSet()
    
    context['formset']=formset
    return render(request, 'pages/ingredient_formset.html', context)

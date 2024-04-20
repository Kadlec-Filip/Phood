import csv
import os
from pathlib import Path
from recipe.models import Recipe, Ingredient, RecipeIngredients

SCRIPTS_DIR = Path(__file__).resolve().parent  # get current dir
recipes_path = os.path.join(SCRIPTS_DIR, 'recipes_init.csv')
ingredients_path = os.path.join(SCRIPTS_DIR, 'ingreditents_init.csv')
rec_ing_path = os.path.join(SCRIPTS_DIR, 'recipe_ingredients_init.csv')

def run():
    rec_file = open(recipes_path)
    rec_csv_file = csv.reader(rec_file, skipinitialspace=True)
    ing_file = open(ingredients_path)
    ing_csv_file = csv.reader(ing_file, skipinitialspace=True)
    recing_file = open(rec_ing_path)
    recing_csv_file = csv.reader(recing_file, skipinitialspace=True)

    # Clean db
    Recipe.objects.all().delete()
    RecipeIngredients.objects.all().delete()
    Ingredient.objects.all().delete()
    
    # --- START --- Generate Carbonara recipe to DB
    for recipe in rec_csv_file:
        carbonara = Recipe.objects.create(title=recipe[0], instructions=recipe[1], picture=recipe[2])
    
    list_of_ings = []
    for ingredient in ing_csv_file:
        i = Ingredient.objects.create(name=ingredient[0])
        list_of_ings.append(i)

    counter = 0
    for recing in recing_csv_file:
        RecipeIngredients.objects.create(recipe_id=carbonara, ingredient_id=list_of_ings[counter], qty=recing[2], unit=recing[3])
        counter+=1
    # --- END --- Generate Carbonara recipe to DB

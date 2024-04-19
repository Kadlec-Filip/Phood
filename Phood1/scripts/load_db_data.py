import csv
import os
from recipe.models import Recipe

def run():
    file = open('recipes_init.csv')
    read_csv_file = csv.reader(file)
    
    # Clean db
    Recipe.objects.all().delete()

    for recipe in read_csv_file:
        print(recipe)
        Recipe.objects.create(title=recipe[0], instructions=recipe[1], ingredients=recipe[2], picture=recipe[3])
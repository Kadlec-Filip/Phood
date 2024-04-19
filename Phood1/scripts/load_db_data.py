import csv
import os
from pathlib import Path
from recipe.models import Recipe

SCRIPTS_DIR = Path(__file__).resolve().parent  # get current dir
file_path = os.path.join(SCRIPTS_DIR, 'recipes_init.csv')

def run():
    file = open(file_path)
    read_csv_file = csv.reader(file, skipinitialspace=True)
    
    # Clean db
    Recipe.objects.all().delete()

    for recipe in read_csv_file:
        print(recipe)
        Recipe.objects.create(title=recipe[0], instructions=recipe[1], ingredients=recipe[2], picture=recipe[3])
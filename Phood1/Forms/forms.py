# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from recipe.models import Recipe, RecipeIngredients, Ingredient
from django import forms

# Comfy idea if you're writing to one Model, but Im saving to three
# class RecipeForm(ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['title', 'picture']

class RecipeForm(forms.Form):
    CATEGORY_UNIT = (
        ('kg', 'kg'),
        ('g', 'g'),
        ('l', 'l'),
        ('tsp', 'tsp'),
        ('tbsp', 'tbsp'),
    )
    CATEGORY_CUISINE = (
        ('Italian', 'Italian'),
        ('French', 'French'),
        ('Asian', 'Asian'),
        ('Indian', 'Indian'),
        ('Czech', 'Czech'),
        ('', ''),
    )
    title       = forms.CharField()
    cuisine     = forms.ChoiceField(choices=CATEGORY_CUISINE)
    time        = forms.IntegerField()
    # picture     = CharField()
    ing_qty     = forms.FloatField()
    ing_unit    = forms.ChoiceField(choices=CATEGORY_UNIT)

IngredientFormSet = forms.modelformset_factory(
    Ingredient, fields=('name',), extra=1
)
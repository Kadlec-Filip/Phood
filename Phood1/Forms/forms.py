# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from recipe.models import Recipe, RecipeIngredients, Ingredient
from django import forms

# Comfy idea if you're writing to one Model, but Im saving to three
# class RecipeForm(ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['title', 'picture']

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields = ['title', 'cuisine', 'time', 'instructions']

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
    instructions= forms.CharField(widget=forms.Textarea)

class IngredientForm(forms.Form):
    class Meta:
        model=Ingredient
        fields = ['name', 'ing_qty', 'ing_unit']
        
    CATEGORY_UNIT = (
        ('kg', 'kg'),
        ('g', 'g'),
        ('l', 'l'),
        ('tsp', 'tsp'),
        ('tbsp', 'tbsp'),
    )
    name        = forms.CharField(label='', widget=forms.TextInput({"placeholder": "ingredient"}))
    ing_qty     = forms.FloatField(label='', widget=forms.TextInput({"placeholder": "quantity"}))
    ing_unit    = forms.ChoiceField(label='', choices=CATEGORY_UNIT)

IngredientFormSet = forms.formset_factory(IngredientForm, extra=1,)

# IngredientFormSet = forms.modelformset_factory(
#     Ingredient, fields=('name',), extra=1
# )
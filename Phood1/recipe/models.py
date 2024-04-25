from django.db import models
 
class Recipe(models.Model):
    CATEGORY_CUISINE = (
        ('Italian', 'Italian'),
        ('French', 'French'),
        ('Asian', 'Asian'),
        ('Indian', 'Indian'),
        ('Czech', 'Czech'),
        ('', ''),
    )
    title           = models.CharField(max_length=100, null=False)
    cuisine         = models.CharField(choices=CATEGORY_CUISINE, default=None)
    time            = models.IntegerField()

    def __str__(self):
        return self.title
    

class Ingredient(models.Model):
    name            = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class RecipeIngredients(models.Model):
    CATEGORY_UNIT = (
        ('kg', 'kg'),
        ('g', 'g'),
        ('l', 'l'),
        ('tsp', 'tsp'),
        ('tbsp', 'tbsp'),
    )

    recipe_id       = models.ForeignKey(Recipe, related_name="recipe", on_delete=models.CASCADE)
    ingredient_id   = models.ForeignKey(Ingredient, related_name="ingredient", on_delete=models.CASCADE)
    qty             = models.FloatField(default=0)
    unit            = models.CharField(null=False, choices=CATEGORY_UNIT, default=None)

    def __str__(self):
        return f"{self.ingredient_id.name} from {self.recipe_id.title}"
    
class Instructions(models.Model):
    rec_id          = models.ForeignKey(Recipe, related_name="rec_id", on_delete=models.CASCADE)
    step_number      = models.IntegerField(default=0)
    step_instruction= models.CharField(max_length=120)

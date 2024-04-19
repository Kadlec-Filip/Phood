from django.db import models

class Recipe(models.Model):
    title       = models.TextField(default='')
    instructions = models.TextField(default='')
    ingredients = models.TextField(default='')
    picture     = models.TextField(default='')  # path to pic
from django.db import models

class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField()
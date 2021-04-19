from django.db import models

# Create your models here.

class Pokemon(models.Model):
    pokemon_number = models.IntegerField()
    name = models.CharField(max_length=255)
    generation = models.IntegerField()
    article_link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    console_owned = models.CharField(max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return f"#{self.pokemon_number} {self.name}"

class RegionalFormPokemon(models.Model):
    form_number = models.IntegerField()
    name = models.CharField(max_length=255)
    generation = models.IntegerField()
    article_link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    console_owned = models.CharField(max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return f"#{self.form_number} {self.name}"

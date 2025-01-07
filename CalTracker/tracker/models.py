from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return f'{self.id}__id__{self.name}'
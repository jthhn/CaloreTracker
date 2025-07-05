from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100,)
    carbs = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}__id__{self.name}'
    
class Consume(models.Model):
    food_consumed = models.ForeignKey(Food,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food_consumed}'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,)
    carbs = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}__id__{self.name}'
    
class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food_consumed}'

class User_goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calorie_goal = models.IntegerField(default=2000)

    def __str__(self):
        return f'{self.user.username}___{self.calorie_goal}'

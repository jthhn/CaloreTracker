from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consumed)

        consume = Consume(food_consumed=consume)
        consume.save()
        foods = Food.objects.all()  
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.all()
    return render(request,'tracker/index.html',{'foods':foods, 'consumed_food':consumed_food})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
       consumed_food.delete()
       return redirect('/') 
    return render(request,'tracker/delete.html')

def add_food(request):

    try:
        if request.method == "POST":
            # get data from form 
            food_name = request.POST.get('name')
            carbs_in_food = request.POST.get('carbs')
            protein_in_food = request.POST.get('protein')
            fat_in_food = request.POST.get('fat')
            calories_in_food = request.POST.get('calories')

            # create the object
            food = Food(name=food_name,
                        carbs=carbs_in_food,
                        protein=protein_in_food,
                        fat=fat_in_food,
                        calories=calories_in_food
            )
            food.save() # save it to the database

            messages.success(request, "Food item added successfully!")

            return redirect('tracker:add_food')
    
    except:
        messages.error(request, 'Try you add proper values.')
    
    return render(request,'tracker/add_food.html')
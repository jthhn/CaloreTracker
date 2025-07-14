from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Food, Consume, User_goal
from django.contrib import messages

# Create your views here.


@login_required(login_url='accounts:login')
def index(request):
    # get all food items

    foods = Food.objects.filter(user=request.user)

    calorie_goal = User_goal.objects.get(user=request.user).calorie_goal

    # check if form is submitted
    if request.method == "POST":
        # get food name from form
        food_consumed = request.POST.get('food_consumed')

        try:
            # fetch the Food object by name
            consume_food = Food.objects.get(user=request.user, name=food_consumed)

            # create Consume object with selected food
            consumed = Consume(user=request.user, food_consumed=consume_food)
            consumed.save()

        except Food.DoesNotExist:
            # if food is not found in DB
            messages.error(request, 'Selected food not found. Please choose from the list.')

        except Exception:
            # handle any other unexpected error
            messages.error(request, 'An error occurred. Please select your meal properly.')

    # get all consumed food to display
    consumed_food = Consume.objects.all()

    # render the index page with foods and consumed list
    return render(request, 'tracker/index.html', {'foods': foods, 'consumed_food': consumed_food, 'calorie_goal': calorie_goal})

@login_required(login_url='accounts:login')
def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
       consumed_food.delete()
       return redirect('/') 
    return render(request,'tracker/delete.html')

@login_required(login_url='accounts:login')
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
            food = Food(user=request.user,
                        name=food_name,
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

@login_required(login_url='accounts:login')
def update_food(request, id):
    try: 
        food = Food.objects.filter(id=id, user=request.user).first() #first is used to make the food to a object other wise it return as a list of results 

        if request.method == "POST":
            # get the action from the submitted form 
            action = request.POST.get('action')

            if action == 'delete':
                try:
                    # delete the food item from database
                    food.delete()
                    messages.success(request, "Food item deleted successfully!")
                    return redirect('/')
                except:
                    messages.error(request, "Nothing to delete.")
                    return redirect('/')

            elif action == 'update':
                try:
                    food_name = request.POST.get('name')    
                    carbs_in_food = request.POST.get('carbs')
                    protein_in_food = request.POST.get('protein')
                    fat_in_food = request.POST.get('fat')
                    calories_in_food = request.POST.get('calories')

                    # update food fields
                    food.name = food_name
                    food.carbs = carbs_in_food
                    food.protein = protein_in_food
                    food.fat = fat_in_food
                    food.calories = calories_in_food

                    food.save()
                    messages.success(request, "Food item updated successfully!")
                    return redirect('/')
                except:
                    messages.error(request, "Add proper values.")
                    return render(request, 'tracker/update_food.html', {'food': food})

            else:
                messages.error(request, "Invalid action.")
                return redirect('/')
                
        # GET request — render update form
        return render(request, 'tracker/update_food.html', {'food': food})

    except Food.DoesNotExist:
        messages.error(request, "Food item not found.")
        return redirect('/')


            
from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed'] 
        consume = Food.objects.get(name=food_consumed)
        user = request.user.id
        consume = Consume(user_id=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()  
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request,'tracker/index.html',{'foods':foods, 'consumed_food':consumed_food})

# @login_required
# def index(request):
#     if request.method == "POST":
#         food_consumed = request.POST['food_consumed']
#         try:
#             # Fetch the Food instance
#             food = Food.objects.get(name=food_consumed)

#             # Use the logged-in user directly
#             consume = Consume(user=request.user, food_consumed=food)
#             consume.save()

#         except Food.DoesNotExist:
#             # Handle cases where the food item does not exist
#             return render(request, 'tracker/index.html', {
#                 'foods': Food.objects.all(),
#                 'consumed_food': Consume.objects.filter(user=request.user),
#                 'error': f"Food item '{food_consumed}' does not exist."
#             })

#     # Fetch all food items and consumed food for the logged-in user
#     foods = Food.objects.all()
#     consumed_food = Consume.objects.filter(user=request.user)

#     return render(request, 'tracker/index.html', {
#         'foods': foods,
#         'consumed_food': consumed_food,
#     })


def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
       consumed_food.delete()
       return redirect('/') 
    return render(request,'tracker/delete.html')
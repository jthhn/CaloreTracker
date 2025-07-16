from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete_consume, name='delete'),
    path('addMeal/',views.add_food,name='add_food'),
    path('update/<int:id>/', views.update_food, name='update_food'),
    path('calgoal/', views.update_calorie_goal, name='calgoal'),
]
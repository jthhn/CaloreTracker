from django.urls import path
from .views import email_login


app_name = 'accounts'
urlpatterns = [
    path('login/', email_login, name='login'),
]
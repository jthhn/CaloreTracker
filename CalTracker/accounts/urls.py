from django.urls import path
from .views import email_login, signup_view


app_name = 'accounts'
urlpatterns = [
    path('login/', email_login, name='login'),
    path('register/', signup_view, name='signup'),
]
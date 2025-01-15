from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
# Create your views here.

def accounts(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == "POST":
        if 'login' in request.POST: # handle login form submission
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request,user)
                return redirect('/') 
            else:
                messages.error(request,'Invalid login credentials')
        
        elif 'register' in request.POST: #handle registration form submission   
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('accounts:accounts')
            else:
                messages.error(request,'Please correct the errors in the registration form')
    return render(request,'accounts/accounts.html',{'login_form':login_form, 'register_form': register_form})

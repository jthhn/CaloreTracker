from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EmailLoginForm, EmailSignUpForm
from django.contrib.auth.models import User

# Create your views here.

def email_login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # authenticate using custom backend
            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid email or password.")

    else:
        form = EmailLoginForm()

    return render(request, 'accounts/login.html', {'form':form})


def signup_view(request):

    if request.method == 'POST':
        form = EmailSignUpForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)

            return redirect('/')
    
     # if GET request or form is invalid
    else:
        form = EmailSignUpForm()

    # render signup page
    return render(request, 'accounts/register.html', {'form': form})

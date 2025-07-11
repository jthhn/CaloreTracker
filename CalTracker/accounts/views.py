from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EmailLoginForm

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

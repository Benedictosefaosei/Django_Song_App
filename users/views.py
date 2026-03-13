from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            user = form.save()

            # Update the profile created by the signal
            user.profile.phone_number = phone_number
            user.profile.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f"Created a new account for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
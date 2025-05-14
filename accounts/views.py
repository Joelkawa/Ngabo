from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(f"User {user.username} registered successfully")
            return redirect('home:home')
        else:
            print("Form is not valid")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


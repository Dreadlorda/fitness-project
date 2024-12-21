from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import UserProfile
from .forms import UserRegistrationForm, UserProfileForm, ContactForm


class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def profile_landing(request):
    return render(request, 'profile_landing.html', {'user': request.user})

@login_required
def profile_update(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile_update.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')  # Display a success message
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def about_us(request):
    return render(request, 'about_us.html')


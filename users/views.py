from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ContactForm
from .models import Profile
from .models import Achievement


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        except Profile.DoesNotExist:
            p_form = ProfileUpdateForm(request.POST, request.FILES)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile = p_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        try:
            p_form = ProfileUpdateForm(instance=request.user.profile)
        except Profile.DoesNotExist:
            p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'workouts/password_change.html'
    success_url = reverse_lazy('password_change_done')
    success_message = "Your password was changed successfully!"

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully updated!')
        return super().form_valid(form)

class AsyncGoalListView(View):
    def get(self, request, *args, **kwargs):
        # Implement the logic for async goal list
        return JsonResponse({'goals': []})

class AsyncAchievementListView(View):
    def get(self, request, *args, **kwargs):
        # Implement the logic for async achievement list
        return JsonResponse({'achievements': []})

class AsyncNutritionDataView(View):
    def get(self, request, *args, **kwargs):
        # Implement the logic for async nutrition data
        return JsonResponse({'nutrition_data': {}})

class AsyncRecommendationsView(View):
    def get(self, request, *args, **kwargs):
        # Implement the logic for async recommendations
        return JsonResponse({'recommendations': []})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            send_mail(
                subject=f"Contact Request from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@example.com'],  # Replace with your email
            )
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect(reverse_lazy('contact'))  # Use reverse_lazy for maintainability
    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {'form': form})  # Move template to 'users'


def index_redirect(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('dashboard'))  # Redirect logged-in users to dashboard
    return redirect(reverse_lazy('index'))  # Redirect non-logged-in users to home/index page

def is_staff(user):
    return user.is_staff

def is_admin(user):
    return user.is_superuser

@login_required
def user_dashboard(request):
    return render(request, 'users/user_dashboard.html')

@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    return render(request, 'users/staff_dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')


class AchievementListView(ListView):
    model = Achievement
    template_name = 'workouts/achievement_list.html'
    context_object_name = 'achievements'

class AchievementCreateView(CreateView):
    model = Achievement
    fields = ['title', 'description', 'awarded_to']
    template_name = 'workouts/achievement_form.html'
    success_url = reverse_lazy('achievement_list')

class AchievementUpdateView(UpdateView):
    model = Achievement
    fields = ['title', 'description']
    template_name = 'workouts/achievement_form.html'
    success_url = reverse_lazy('achievement_list')

class AchievementDeleteView(DeleteView):
    model = Achievement
    template_name = 'workouts/achievement_confirm_delete.html'
    success_url = reverse_lazy('achievement_list')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Goal
from .forms import GoalForm

class GoalListView(LoginRequiredMixin, generic.ListView):
    model = Goal
    template_name = 'workouts/goal_list.html'
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalCreateView(LoginRequiredMixin, generic.CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'workouts/goal_form.html'
    success_url = reverse_lazy('goal-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'workouts/goal_form.html'
    success_url = reverse_lazy('goal-list')

class GoalDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Goal
    template_name = 'workouts/goal_confirm_delete.html'
    success_url = reverse_lazy('goal-list')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from .models import Goal
from nutrition.models import ProgressLog
from workouts.models import Workout

class AnalyticsView(LoginRequiredMixin):
    template_name = 'analytics/dashboard.html'

    def get(self, request):
        # Aggregate user data
        total_goals = Goal.objects.filter(user=request.user).count()
        total_progress = ProgressLog.objects.filter(user=request.user).aggre...
        total_workouts = Workout.objects.filter(user=request.user).count()

        context = {
            'total_goals': total_goals,
            'total_progress': total_progress,
            'total_workouts': total_workouts,
        }
        return render(request, self.template_name, context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Workout, Streak, Badge
from django.utils import timezone
from django.contrib import messages

@login_required
def update_streak(request):
    streak, created = Streak.objects.get_or_create(user=request.user)
    streak.update_streak()
    messages.success(request, f"Your streak has been updated! Current Streak...
    return redirect('workout-list')

@login_required
def award_badges(request):
    streak, _ = Streak.objects.get_or_create(user=request.user)
    if streak.current_streak == 7:  # Example condition for 7-day streak
        badge, created = Badge.objects.get_or_create(name='7-Day Streak', de...
        if created:
            badge.save()
        messages.success(request, "Congratulations! You've earned the '7-Day...
    return redirect('workout-list')

@login_required
def leaderboard(request):
    top_users = Streak.objects.order_by('-current_streak')[:10]  # Top 10 us...
    context = {'top_users': top_users}
    return render(request, 'workouts/leaderboard.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Workout, Streak, Badge
from django.utils import timezone
from django.contrib import messages

@login_required
def update_streak(request):
    streak, created = Streak.objects.get_or_create(user=request.user)
    streak.update_streak()
    messages.success(request, f"Your streak has been updated! Current Streak...
    return redirect('workout-list')

@login_required
def award_badges(request):
    streak, _ = Streak.objects.get_or_create(user=request.user)
    if streak.current_streak == 7:  # Example condition for 7-day streak
        badge, created = Badge.objects.get_or_create(name='7-Day Streak', de...
        if created:
            badge.save()
        messages.success(request, "Congratulations! You've earned the '7-Day...
    return redirect('workout-list')

@login_required
def leaderboard(request):
    top_users = Streak.objects.order_by('-current_streak')[:10]  # Top 10 us...
    context = {'top_users': top_users}
    return render(request, 'workouts/leaderboard.html', context)

from .models import Notification

@login_required
def update_streak(request):
    streak, created = Streak.objects.get_or_create(user=request.user)
    streak.update_streak()
    Notification.objects.create(user=request.user, message=f"Your streak has...
    messages.success(request, f"Your streak has been updated! Current Streak...
    return redirect('workout-list')

@login_required
def award_badges(request):
    streak, _ = Streak.objects.get_or_create(user=request.user)
    if streak.current_streak == 7:  # Example condition for 7-day streak
        badge, created = Badge.objects.get_or_create(name='7-Day Streak', de...
        if created:
            badge.save()
        Notification.objects.create(user=request.user, message="Congratulati...
        messages.success(request, "Congratulations! You've earned the '7-Day...
    return redirect('workout-list')

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from .models import Workout, Streak

@login_required
def generate_progress_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="progress_report...

    # Create the PDF object
    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Progress Report for {request.user.username}")

    # Fetch streak details
    streak, _ = Streak.objects.get_or_create(user=request.user)
    p.drawString(100, 770, f"Current Streak: {streak.current_streak} days")
    p.drawString(100, 750, f"Longest Streak: {streak.longest_streak} days")

    # Fetch workout details
    workouts = Workout.objects.filter(user=request.user)
    y = 730
    p.drawString(100, y, "Workout Summary:")
    for workout in workouts:
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
        p.drawString(100, y, f"{workout.name}: {workout.duration} mins, {wor...

    p.showPage()
    p.save()
    return response

from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Workout

@login_required
def activity_recommendations(request):
    user_workouts = Workout.objects.filter(user=request.user)
    avg_duration = user_workouts.aggregate(Avg('duration'))['duration__avg']...
    avg_calories = user_workouts.aggregate(Avg('calories_burned'))['calories...

    recommendations = []
    if avg_duration < 30:
        recommendations.append("Try increasing your workout duration to at l...
    if avg_calories < 300:
        recommendations.append("Focus on high-intensity workouts to burn mor...
    if user_workouts.count() < 3:
        recommendations.append("Aim to work out at least 3 times a week to b...

    context = {
        'recommendations': recommendations,
        'avg_duration': avg_duration,
        'avg_calories': avg_calories,
    }
    return render(request, 'workouts/recommendations.html', context)

from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Workout, Streak

@login_required
def dashboard(request):
    streak, _ = Streak.objects.get_or_create(user=request.user)
    total_calories = Workout.objects.filter(user=request.user).aggregate(Sum...
    total_workouts = Workout.objects.filter(user=request.user).count()

    context = {
        'streak': streak,
        'total_calories': total_calories,
        'total_workouts': total_workouts,
    }
    return render(request, 'workouts/dashboard.html', context)

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Achievement

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

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Normally you would process the data here (e.g., send an email)
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'workouts/contact.html', {'form': form})

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'workouts/password_change.html'
    success_url = reverse_lazy('password_change_done')
    success_message = "Your password was changed successfully!"

from django.shortcuts import redirect
from django.urls import reverse

def index_redirect(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))  # Redirect logged-in users to dashboard
    return redirect(reverse('index'))  # Redirect non-logged-in users to home/index page

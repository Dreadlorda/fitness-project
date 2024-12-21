from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Workout


class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workout_list.html"
    context_object_name = "workouts"

    def get_queryset(self):
        # Only show workouts for the currently logged-in user
        return Workout.objects.filter(user=self.request.user)


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    template_name = "workout_form.html"
    fields = ['exercise_type', 'sets', 'reps', 'duration', 'date']
    success_url = reverse_lazy('workout-list')

    def form_valid(self, form):
        # Set the user of the workout to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

class WorkoutUpdateView(UpdateView):
    model = Workout
    template_name = 'workout_form.html'
    fields = ['exercise_type', 'sets', 'reps', 'duration', 'date']
    success_url = reverse_lazy('workout-list')

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workout_confirm_delete.html'
    success_url = reverse_lazy('workout-list')
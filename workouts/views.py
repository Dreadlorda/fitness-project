
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Workout

class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts/workout_list.html'

class WorkoutCreateView(CreateView):
    model = Workout
    fields = ['name', 'duration']
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workout-list')

class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = ['name', 'duration']
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workout-list')

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workouts/workout_confirm_delete.html'
    success_url = reverse_lazy('workout-list')

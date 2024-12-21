from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Goal

class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = "goal_list.html"
    context_object_name = "goals"

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    template_name = "goal_form.html"
    fields = ['title', 'description', 'goal_type', 'target', 'progress', 'deadline']
    success_url = reverse_lazy('goal-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    template_name = "goal_form.html"
    fields = ['title', 'description', 'goal_type', 'target', 'progress', 'deadline']
    success_url = reverse_lazy('goal-list')

class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = "goal_confirm_delete.html"
    success_url = reverse_lazy('goal-list')

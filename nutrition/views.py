from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import NutritionLog

class NutritionLogListView(LoginRequiredMixin, ListView):
    model = NutritionLog
    template_name = "nutrition_log_list.html"
    context_object_name = "logs"

    def get_queryset(self):
        return NutritionLog.objects.filter(user=self.request.user)

class NutritionLogCreateView(LoginRequiredMixin, CreateView):
    model = NutritionLog
    template_name = "nutrition_log_form.html"
    fields = ['name', 'calories', 'protein', 'carbs', 'fat', 'date']
    success_url = reverse_lazy('nutrition-log-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NutritionLogUpdateView(UpdateView):
    model = NutritionLog
    fields = ['name', 'calories', 'protein', 'carbs', 'fat', 'date']
    template_name = 'nutrition_log_form.html'
    success_url = reverse_lazy('nutrition-log-list')

class NutritionLogDeleteView(DeleteView):
    model = NutritionLog
    template_name = 'nutrition_confirm_delete.html'
    success_url = reverse_lazy('nutrition-log-list')


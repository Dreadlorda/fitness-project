from django import forms
from .models import NutritionLog


class NutritionLogCreateForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['meal', 'calories', 'protein', 'carbs', 'fat']

class NutritionLogUpdateForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['meal', 'calories', 'protein', 'carbs', 'fat']

class SearchNutritionLogForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=False, label="Search...")
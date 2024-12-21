from django import forms
from .models import NutritionLog

class NutritionLogForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['name', 'calories', 'protein', 'carbs', 'fat', 'date']

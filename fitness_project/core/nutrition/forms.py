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

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    age = forms.IntegerField(required=True)

class FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea, label="Your Feedback")

class UserSettingsForm(forms.Form):
    enable_notifications = forms.BooleanField(required=False)
    daily_calorie_goal = forms.IntegerField(min_value=0)

    def save(self, user):
        user.profile.enable_notifications = self.cleaned_data['enable_notifications']
        user.profile.daily_calorie_goal = self.cleaned_data['daily_calorie_goal']
        user.profile.save()

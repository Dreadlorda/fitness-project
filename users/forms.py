from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserSettingsForm(forms.Form):
    enable_notifications = forms.BooleanField(required=False)
    daily_calorie_goal = forms.IntegerField(min_value=0, required=False)

    def save(self, user):
        profile, created = Profile.objects.get_or_create(user=user)
        profile.enable_notifications = self.cleaned_data['enable_notifications']
        profile.daily_calorie_goal = self.cleaned_data['daily_calorie_goal']
        profile.save()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")
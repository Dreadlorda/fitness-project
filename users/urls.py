from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import register, profile_update, CustomLoginView, profile_landing, logout_user, about_us, contact_us

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile_landing, name='profile'),  # Profile landing page
    path('profile/update/', profile_update, name='profile-update'),  # Profile update page
    path('logout/', logout_user, name='logout'),
    path('contact/', contact_us, name='contact-us'),
    path('about/', about_us, name='about-us'),
]

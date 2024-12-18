
from django.urls import path
from . import views

urlpatterns = [
    path('progress/', views.ProgressLogListView.as_view(), name='progress-log'),
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
    path('settings/', views.UserSettingsView.as_view(), name='user-settings'),
]

from django.contrib import admin
from django.urls import path, include
from async_rest_integration.async_rest_integration import AsyncGoalAPIView, AsyncWorkoutAPIView

urlpatterns = [
    path('goals/', AsyncGoalAPIView.as_view(), name='async-goals-api'),
    path('workouts/', AsyncWorkoutAPIView.as_view(), name='async-workouts-api'),
]

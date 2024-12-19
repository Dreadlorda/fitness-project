
from django.urls import path
from .views import WorkoutListView, WorkoutCreateView, WorkoutUpdateView, WorkoutDeleteView

urlpatterns = [
    path('', WorkoutListView.as_view(), name='workout-list'),
    path('create/', WorkoutCreateView.as_view(), name='workout-create'),
    path('<int:pk>/update/', WorkoutUpdateView.as_view(), name='workout-update'),
    path('<int:pk>/delete/', WorkoutDeleteView.as_view(), name='workout-delete'),
]

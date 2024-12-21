from django.urls import path
from .views import GoalListView, GoalCreateView, GoalUpdateView, GoalDeleteView

urlpatterns = [
    path('', GoalListView.as_view(), name='goal-list'),
    path('create/', GoalCreateView.as_view(), name='goal-create'),
    path('<int:pk>/update/', GoalUpdateView.as_view(), name='goal-update'),
    path('<int:pk>/delete/', GoalDeleteView.as_view(), name='goal-delete'),
]

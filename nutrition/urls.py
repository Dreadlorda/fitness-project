from django.urls import path
from .views import NutritionLogListView, NutritionLogCreateView, NutritionLogUpdateView, NutritionLogDeleteView

urlpatterns = [
    path('', NutritionLogListView.as_view(), name='nutrition-log-list'),
    path('create/', NutritionLogCreateView.as_view(), name='nutrition-log-create'),
    path('<int:pk>/update/', NutritionLogUpdateView.as_view(), name='nutrition-log-update'),
    path('<int:pk>/delete/', NutritionLogDeleteView.as_view(), name='nutrition-log-delete'),
]
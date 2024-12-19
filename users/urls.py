from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    contact_view,
    index_redirect,
    user_dashboard,
    staff_dashboard,
    admin_dashboard,
)
from users.views import (
    CustomPasswordChangeView,
    AsyncGoalListView,
    AsyncAchievementListView,
    AsyncNutritionDataView,
    AsyncRecommendationsView
)
from views import (  # Add this import
    AchievementListView,
    AchievementCreateView,
    AchievementUpdateView,
    AchievementDeleteView,
)

# The rest of your urlpatterns remain the same

urlpatterns = [
    path('achievements/', AchievementListView.as_view(), name='achievement_list'),
    path('achievements/create/', AchievementCreateView.as_view(), name='achievement_create'),
    path('achievements/<int:pk>/update/', AchievementUpdateView.as_view(), name='achievement_update'),
    path('achievements/<int:pk>/delete/', AchievementDeleteView.as_view(), name='achievement_delete'),
    path('contact/', contact_view, name='contact'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='workouts/password_change_done.html'), name='password_change_done'),
    path('', index_redirect, name='index_redirect'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('dashboard/staff/', staff_dashboard, name='staff_dashboard'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('async-fitness_project.core.goals/', AsyncGoalListView.as_view(), name='async_goals'),
    path('async-achievements/', AsyncAchievementListView.as_view(), name='async_achievements'),
    path('async-fitness_project.core.nutrition/', AsyncNutritionDataView.as_view(), name='async_nutrition_data'),
    path('async-recommendations/', AsyncRecommendationsView.as_view(), name='async_recommendations'),
]


from django.urls import path
from .views import AchievementListView, AchievementCreateView, AchievementUp...

urlpatterns = [
    path('achievements/', AchievementListView.as_view(), name='achievement_l...
    path('achievements/create/', AchievementCreateView.as_view(), name='achi...
    path('achievements/<int:pk>/update/', AchievementUpdateView.as_view(), n...
    path('achievements/<int:pk>/delete/', AchievementDeleteView.as_view(), n...
]

from django.urls import path
from .views import contact_view

urlpatterns += [
    path('contact/', contact_view, name='contact'),
]

from django.urls import path
from .views import CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns += [
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='workouts/password_change_done.html'), name='password_change_done'),
]

from .views import index_redirect

urlpatterns += [
    path('', index_redirect, name='index_redirect'),
]

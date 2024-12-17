
# Add 'allauth' and providers in settings.py
INSTALLED_APPS += [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# SITE_ID configuration
SITE_ID = 1

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Social account providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    },
        'SCOPE': ['user_profile', 'user_media'],
        'AUTH_PARAMS': {'auth_type': 'rerequest'},
    }
}

# URLs for allauth
urlpatterns += [
    path('accounts/', include('allauth.urls')),
]

# Email Backend Configuration (for sending notifications)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-email-password'  # Replace with your password

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Celery Beat Scheduler
INSTALLED_APPS += ['django_celery_beat']

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-daily-goal-reminders': {
        'task': 'workouts.tasks.send_goal_reminder',
        'schedule': crontab(hour=8, minute=0),  # Runs daily at 8 AM
    },
}

# Admin configuration for UserProfile
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'bio')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)
    ordering = ('user',)

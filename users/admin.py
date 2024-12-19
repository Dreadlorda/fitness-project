from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Achievement


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('age', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('age', 'bio')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'awarded_to', 'awarded_at')
    list_filter = ('awarded_at', 'awarded_to')
    search_fields = ('title', 'awarded_to__username')
    ordering = ('-awarded_at',)


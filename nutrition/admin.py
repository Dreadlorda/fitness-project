
from django.contrib import admin
from .models import NutritionLog

class NutritionLogAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at',)
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="nutrition_l...
        writer = csv.writer(response)
        writer.writerow(['Name', 'Calories', 'User', 'Created At'])
        for log in queryset:
            writer.writerow([log.name, log.calories, log.user.username, log....
        return response

    export_to_csv.short_description = "Export selected logs to CSV"

admin.site.register(NutritionLog, NutritionLogAdmin)

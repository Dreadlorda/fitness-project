
from rest_framework import serializers
from fitness_project.core.nutrition.models import NutritionLog

class NutritionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionLog
        fields = '__all__'

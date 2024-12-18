
from rest_framework import serializers
from fitness_project.core.workouts.models import Workout, Achievement


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'awarded_to', 'awarded_at']

# fitness_project/core/goals/serializers.py
from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'user', 'goal_type', 'target', 'progress', 'deadline', 'created_at']

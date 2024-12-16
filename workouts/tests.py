
from django.test import TestCase
from .models import Workout

class WorkoutModelTest(TestCase):

    def setUp(self):
        self.workout = Workout.objects.create(
            name="Test Workout",
            duration=60,
            calories_burned=500
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Test Workout")
        self.assertEqual(self.workout.duration, 60)
        self.assertEqual(self.workout.calories_burned, 500)

class WorkoutViewTest(TestCase):

    def test_workouts_api_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

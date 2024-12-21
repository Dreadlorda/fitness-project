from audioop import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Workout

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_workout(self):
        response = self.client.post(reverse('workout-create'), {
            'exercise_type': 'Running',
            'sets': 3,
            'reps': 10,
            'duration': 30,
            'date': '2024-12-21'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Workout.objects.count(), 1)

    def test_workout_list_view(self):
        response = self.client.get(reverse('workouts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workout_list.html')

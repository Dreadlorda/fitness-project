from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from fitness_project.core.workouts.models import Workout

class UserCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.workout = Workout.objects.create(name='Test Workout', created_by=self.user)

    def test_user_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_workout_creation(self):
        response = self.client.post(reverse('workout_create'), {'name': 'New Workout'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Workout.objects.count(), 2)

    def test_workout_update(self):
        response = self.client.post(reverse('workout_update', args=[self.workout.id]), {'name': 'Updated Workout'})
        self.assertEqual(response.status_code, 200)
        self.workout.refresh_from_db()
        self.assertEqual(self.workout.name, 'Updated Workout')

    def test_workout_deletion(self):
        response = self.client.post(reverse('workout_delete', args=[self.workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Workout.objects.count(), 0)

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from nutrition.models import NutritionLog
from workouts.models import Workout

class WorkoutAndNutritionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='...
        self.client.login(username='testuser', password='password')
        self.workout = Workout.objects.create(user=self.user, name='Workout ...
        self.nutrition_log = NutritionLog.objects.create(user=self.user, mea...

    def test_workout_list_view(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.workout.name)

    def test_nutrition_list_view(self):
        response = self.client.get(reverse('nutritionlog-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.nutrition_log.meal)

    def test_api_workout_create(self):
        response = self.client.post(reverse('workout-list'), {'name': 'Worko...
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Workout.objects.count(), 2)

    def test_api_nutrition_create(self):
        response = self.client.post(reverse('nutritionlog-list'), {'meal': '...
        self.assertEqual(response.status_code, 201)
        self.assertEqual(NutritionLog.objects.count(), 2)

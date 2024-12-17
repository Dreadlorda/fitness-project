
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from workouts.models import Achievement

class APITestCases(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="...
        self.client.force_authenticate(user=self.user)
        self.achievement = Achievement.objects.create(title="Test Achievemen...

    def test_get_achievements(self):
        response = self.client.get(reverse('achievement_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('achievement_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_post(self):
        response = self.client.post(reverse('achievement_list'), {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

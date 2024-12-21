from audioop import reverse
from django.test import TestCase, Client
from rest_framework.authtoken.admin import User

from .models import Goal
class GoalTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_goal(self):
        response = self.client.post(reverse('goal-create'), {
            'name': 'Lose Weight',
            'description': 'Lose 5kg in 3 months',
            'target_date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Goal.objects.count(), 1)

    def test_goal_list_view(self):
        response = self.client.get(reverse('goals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/goal_list.html')

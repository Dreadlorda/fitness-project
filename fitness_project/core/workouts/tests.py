from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Goal

class GoalTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.goal = Goal.objects.create(user=self.user, goal_type='steps', target=10000, progress=5000, deadline='2022-12-31')

    def test_goal_list_view(self):
        response = self.client.get(reverse('goal-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.goal.goal_type)

    def test_goal_create_view(self):
        response = self.client.post(reverse('goal-create'), {
            'goal_type': 'calories', 'target': 2000, 'progress': 1000, 'deadline': '2022-12-31'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Goal.objects.count(), 2)

    def test_goal_update_view(self):
        response = self.client.post(reverse('goal-update', args=[self.goal.id]), {
            'goal_type': 'steps', 'target': 12000, 'progress': 6000, 'deadline': '2022-12-31'
        })
        self.goal.refresh_from_db()
        self.assertEqual(self.goal.target, 12000)

    def test_goal_delete_view(self):
        response = self.client.post(reverse('goal-delete', args=[self.goal.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Goal.objects.count(), 0)
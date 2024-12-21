from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import NutritionLog

class NutritionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_nutrition_log(self):
        response = self.client.post(reverse('nutrition-log-create'), {
            'name': 'Test Meal',
            'calories': 500,
            'protein': 20,
            'carbs': 50,
            'fat': 10,
            'date': '2024-12-21'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(NutritionLog.objects.count(), 1)

    def test_nutrition_list_view(self):
        response = self.client.get(reverse('nutrition-log-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nutrition/nutrition_log_list.html')

    def test_update_nutrition_log(self):
        log = NutritionLog.objects.create(user=self.user, name='Test Meal', calories=500, protein=20, carbs=50, fat=10, date='2024-12-21')
        response = self.client.post(reverse('nutrition-log-update', args=[log.id]), {
            'name': 'Updated Meal',
            'calories': 400,
            'protein': 15,
            'carbs': 45,
            'fat': 8,
            'date': '2024-12-22'
        })
        self.assertEqual(response.status_code, 302)
        log.refresh_from_db()
        self.assertEqual(log.name, 'Updated Meal')


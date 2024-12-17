
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import NutritionLog

class NutritionLogTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.nutrition_log = NutritionLog.objects.create(
            user=self.user, meal="Breakfast", calories=400, protein=20, carbs=50, fat=10
        )

    def test_nutrition_log_creation(self):
        self.assertEqual(self.nutrition_log.meal, "Breakfast")
        self.assertEqual(self.nutrition_log.calories, 400)

    def test_authenticated_nutrition_log_list(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("nutritionlog-list"))
        self.assertEqual(response.status_code, 200)

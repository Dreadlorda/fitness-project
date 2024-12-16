
from django.test import TestCase
from .models import NutritionLog

class NutritionLogModelTest(TestCase):

    def setUp(self):
        self.log = NutritionLog.objects.create(
            food="Test Food",
            calories=300,
            protein=10,
            carbs=20,
            fats=5
        )

    def test_nutrition_log_creation(self):
        self.assertEqual(self.log.food, "Test Food")
        self.assertEqual(self.log.calories, 300)
        self.assertEqual(self.log.protein, 10)
        self.assertEqual(self.log.carbs, 20)
        self.assertEqual(self.log.fats, 5)

class NutritionLogViewTest(TestCase):

    def test_nutrition_api_list(self):
        response = self.client.get('/api/nutrition/')
        self.assertEqual(response.status_code, 200)

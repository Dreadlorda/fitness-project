from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')  # Adjusted template name

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  # Login redirects to profile or home

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_landing.html')  # Adjusted template name

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect to home

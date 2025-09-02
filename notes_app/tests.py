from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from notes_app.models import Note

# Create your tests here.
class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'password_repeat': 'testpassword123'
        }

        response = self.client.post('/api/auth/users/', data, format='json')
        self.assertEqual(response.status_code, 201)
        User = get_user_model()
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'test@example.com')


    def test_user_login(self):
        User = get_user_model()
        User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='test@example.com'
        )

        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }

        response = self.client.post('/api/auth/jwt/create/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertGreater(len(response.data['access']), 20)


    def test_unauthorized_cannot_create_note(self):
        self.client.logout()

        response = self.client.post('/api/notes/', {
            'title': 'Тест',
            'content': 'Содержание'
        }, format='json')


        self.assertEqual(response.status_code, 401)
        self.assertEqual(Note.objects.count(), 0)
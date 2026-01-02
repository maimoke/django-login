from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class UserViewTests(TestCase):

    def setUp(self):
        self.password = "testpass123"
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password=self.password
        )

    def test_index_requires_login(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 302)
    
    def test_index_logged_in(self):
        self.client.login(username="testuser", password=self.password)
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    def test_sign_in_success(self):
        response = self.client.post(
            '/user/sign-in/',
            {
                "username": "testuser",
                "password": self.password
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/')

    def test_sign_in_failure(self):
        response = self.client.post(
            '/user/sign-in/',
            {
                "username": "testuser",
                "password": "wrongpass"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in not successful")
    
    def test_sign_up_success(self):
        response = self.client.post(
            '/user/sign-up/',
            {
                "username": "newuser",
                "email": "new@example.com",
                "password": "newpass123",
                "confirm": "newpass123"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_sign_up_password_mismatch(self):
        response = self.client.post(
            '/user/sign-up/',
            {
                "username": "baduser",
                "email": "bad@example.com",
                "password": "pass1",
                "confirm": "pass2"
            }
        )
        self.assertContains(response, "Sign up not successful")

    def test_sign_out(self):
        self.client.login(username="testuser", password=self.password)
        response = self.client.get('/user/sign-out/')
        self.assertEqual(response.status_code, 302)

from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User


class Login:
    def login_testuser1(self):
        self.client.login(username="testuser", password="your_password")


class UserCRUDTest(Login, TestCase):
    fixtures = ["Task_manager_fixture.json"]

    def test_registration_user(self):
        response = self.client.post(
            reverse("registration"),
            {
                "username": "testuser222",
                "password1": "111",
                "password2": "111",
                "first_name": "test_first_name",
                "last_name": "test_last_name",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("login"))
        self.assertTrue(User.objects.filter(username="testuser222").exists())

    def test_update_user(self):
        updated_data = {
            "username": "testuser45",
            "password1": "111",
            "password2": "111",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
        }
        self.login_testuser1()
        response = self.client.post(reverse("update_user", args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse("users"))
        user = User.objects.get(pk=1)
        user.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(user.username, "testuser45")
        self.assertEqual(user.first_name, "test_first_name")
        self.assertEqual(user.last_name, "test_last_name")
        self.assertTrue(user.check_password("111"))

    def test_delete_user(self):
        self.login_testuser1()
        self.assertTrue(User.objects.filter(id=1).exists())
        response = self.client.post(reverse("delete_user", args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(id=1).exists())

        self.client.login(username="testuser4", password="your_password")
        response = self.client.post(reverse("delete_user", args=[4]))
        messages = list(get_messages(response.wsgi_request))
        self.assertFalse(User.objects.filter(id=4).exists())
        self.assertTrue(messages)

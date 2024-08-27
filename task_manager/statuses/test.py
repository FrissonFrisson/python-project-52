from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from task_manager.statuses.models import TaskStatus


class Login:
    def login_testuser1(self):
        self.client.login(username="testuser", password="your_password")


class StatusCRUDTest(Login, TestCase):
    fixtures = ["Task_manager_fixture.json"]

    def test_create_status(self):
        response = self.client.post(
            reverse("create_status"),
            {
                "name": "status",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertRedirects(response, expected_url=reverse("login"))

        self.login_testuser1()
        response = self.client.post(
            reverse("create_status"),
            {
                "name": "status",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("statuses_list"))
        self.assertTrue(TaskStatus.objects.filter(name="status").exists())

    def test_delete_status(self):
        self.login_testuser1()
        response = self.client.post(reverse("delete_status", args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("statuses_list"))
        self.assertFalse(TaskStatus.objects.filter(id=1).exists())
        self.assertTrue(messages)

    def test_update_status(self):
        updated_data = {
            "name": "newname",
        }
        self.login_testuser1()
        response = self.client.post(reverse("update_status", args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse("statuses_list"))
        status = TaskStatus.objects.get(pk=1)
        status.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(status.name, "newname")

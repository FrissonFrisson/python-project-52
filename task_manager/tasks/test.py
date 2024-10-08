from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from task_manager.tasks.models import Task


class Login:
    def login_testuser1(self):
        self.client.login(username="testuser", password="your_password")


class TaskCRUDTest(Login, TestCase):
    fixtures = ["Task_manager_fixture.json"]

    def test_create_task(self):
        self.login_testuser1()
        response = self.client.post(
            reverse("create_task"),
            {
                "name": "New Task",
                "author": 2,
                "executor": 3,
                "labels": [2],
                "description": "Task description",
                "status": 2,
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("tasks_list"))
        self.assertTrue(Task.objects.filter(name="New Task").exists())

    def test_delete_task(self):
        self.login_testuser1()
        response = self.client.post(reverse("delete_task", args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("tasks_list"))
        self.assertTrue(Task.objects.filter(id=1).exists())
        self.assertTrue(messages)

        response = self.client.post(reverse("delete_task", args=[2]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("tasks_list"))
        self.assertFalse(Task.objects.filter(id=2).exists())
        self.assertTrue(messages)

    def test_update_task(self):
        updated_data = {
            "name": "Updated Task",
            "author": 2,
            "executor": 3,
            "labels": [2],
            "description": "Updated description",
            "status": 2,
        }
        self.login_testuser1()
        response = self.client.post(
            reverse("update_task", args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse("tasks_list"))
        task = Task.objects.get(pk=1)
        task.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(task.name, "Updated Task")

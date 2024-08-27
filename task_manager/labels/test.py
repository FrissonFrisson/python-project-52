from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from task_manager.labels.models import Label


class Login:
    def login_testuser1(self):
        self.client.login(username="testuser", password="your_password")


class LabelCRUDTest(Login, TestCase):
    fixtures = ["Task_manager_fixture.json"]

    def test_create_label(self):
        response = self.client.post(
            reverse("create_label"),
            {
                "name": "label",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertRedirects(response, expected_url=reverse("login"))

        self.login_testuser1()
        response = self.client.post(
            reverse("create_label"),
            {
                "name": "label",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("labels_list"))
        self.assertTrue(Label.objects.filter(name="label").exists())

    def test_delete_label(self):
        self.login_testuser1()
        response = self.client.post(reverse("delete_label", args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse("labels_list"))
        self.assertFalse(Label.objects.filter(id=1).exists())
        self.assertTrue(messages)

    def test_update_label(self):
        updated_data = {
            "name": "newname",
        }
        self.login_testuser1()
        response = self.client.post(
            reverse("update_label", args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse("labels_list"))
        label = Label.objects.get(pk=1)
        label.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(label.name, "newname")

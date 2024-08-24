from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from task_manager.models import TaskStatus, Label, Task


class Login():

    def login_testuser1(self):
        self.client.login(username='testuser', password='your_password')


class TaskCRUDTest(Login, TestCase):

    fixtures = ['Task_manager_fixture.json']

    def test_create_task(self):
        self.login_testuser1()
        response = self.client.post(reverse('create_task'), {
            "name": "New Task",
            "author": 2,
            "executor": 3,
            "label": [2],
            "description": "Task description",
            "status": 2,
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('tasks_list'))
        self.assertTrue(Task.objects.filter(name='New Task').exists())

    def test_delete_task(self):
        self.login_testuser1()
        response = self.client.post(reverse('delete_task', args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('tasks_list'))
        self.assertTrue(Task.objects.filter(id=1).exists())
        self.assertTrue(messages)
        response = self.client.post(reverse('delete_task', args=[2]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('tasks_list'))
        self.assertFalse(Task.objects.filter(id=2).exists())
        self.assertTrue(messages)

    def test_update_task(self):
        updated_data = {
            "name": "Updated Task",
            "author": 2,
            "executor": 3,
            "label": [2],
            "description": "Updated description",
            "status": 2,
        }
        self.login_testuser1()
        response = self.client.post(reverse('update_task', args=[1]), updated_data)  # Убедитесь, что ID задачи существует в ваших фикстурах
        self.assertRedirects(response, expected_url=reverse('tasks_list'))
        task = Task.objects.get(pk=1)
        task.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(task.name, 'Updated Task')


class LabelCRUDTest(Login, TestCase):

    fixtures = ['Task_manager_fixture.json']

    def test_create_label(self):
        response = self.client.post(reverse('create_label'), {
            "name": "label",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertRedirects(response, expected_url=reverse('login'))
        self.login_testuser1()
        response = self.client.post(reverse('create_label'), {
            "name": "label",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('labels_list'))
        self.assertTrue(Label.objects.filter(name='label').exists())

    def test_delete_label(self):
        self.login_testuser1()
        response = self.client.post(reverse('delete_label', args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('labels_list'))
        self.assertFalse(Label.objects.filter(id=1).exists())
        self.assertTrue(messages)

    def test_update_label(self):
        updated_data = {
            "name": "newname",
        }
        self.login_testuser1()
        response = self.client.post(reverse('update_label', args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse('labels_list'))
        label = Label.objects.get(pk=1)
        label.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(label.name, 'newname')


class StatusCRUDTest(Login, TestCase):

    fixtures = ['Task_manager_fixture.json']

    def test_create_status(self):
        response = self.client.post(reverse('create_status'), {
            "name": "status",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertRedirects(response, expected_url=reverse('login'))
        self.login_testuser1()
        response = self.client.post(reverse('create_status'), {
            "name": "status",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('statuses_list'))
        self.assertTrue(TaskStatus.objects.filter(name='status').exists())

    def test_delete_status(self):
        self.login_testuser1()
        response = self.client.post(reverse('delete_status', args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('statuses_list'))
        self.assertFalse(TaskStatus.objects.filter(id=1).exists())
        self.assertTrue(messages)

    def test_update_status(self):
        updated_data = {
            "name": "newname",
        }
        self.login_testuser1()
        response = self.client.post(reverse('update_status', args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse('statuses_list'))
        Task = TaskStatus.objects.get(pk=1)
        Task.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(Task.name, 'newname')


class UserCRUDTest(Login, TestCase):

    fixtures = ['Task_manager_fixture.json']

    def test_registration_user(self):
        response = self.client.post(reverse('registration'), {
            "username": "testuser222",
            "password1": "111",
            "password2": "111",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser222').exists())

    def test_update_user(self):
        updated_data = {
            "username": "testuser45",
            "password1": "111",
            "password2": "111",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
        }
        self.login_testuser1()
        response = self.client.post(reverse('update_user', args=[1]), updated_data)
        self.assertRedirects(response, expected_url=reverse('users'))
        user = User.objects.get(pk=1)
        user.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(user.username, 'testuser45')
        self.assertEqual(user.first_name, 'test_first_name')
        self.assertEqual(user.last_name, 'test_last_name')
        self.assertTrue(user.check_password('111'))

    def test_delete_user(self):
        self.login_testuser1()
        self.assertTrue(User.objects.filter(id=1).exists())
        response = self.client.post(reverse('delete_user', args=[1]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(id=1).exists())
        self.client.login(username='testuser4', password='your_password')
        response = self.client.post(reverse('delete_user', args=[4]))
        messages = list(get_messages(response.wsgi_request))
        self.assertFalse(User.objects.filter(id=4).exists())
        self.assertTrue(messages)

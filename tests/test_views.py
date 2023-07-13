from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.shortcuts import get_object_or_404
from tasks.models import Task, Tag


class CompleteTaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        tag = Tag.objects.create(title="testtag")

        self.task = Task.objects.create(
            content='Test Task',
            performance=False
        )
        self.task.tags.add(tag.id)
        self.task.save()

    def test_complete_task(self):
        self.client.force_login(self.user)
        url = reverse("tasks:complete_task", kwargs={'pk': self.task.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        updated_task = get_object_or_404(Task, id=self.task.pk)
        self.assertTrue(updated_task.performance)


class CancelTaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.task = Task.objects.create(
            content='Test Task',
            performance=True
        )

    def test_cancel_task(self):
        self.client.force_login(self.user)
        url = reverse("tasks:cancel_task", kwargs={'pk': self.task.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        updated_task = get_object_or_404(Task, id=self.task.pk)
        self.assertFalse(updated_task.performance)

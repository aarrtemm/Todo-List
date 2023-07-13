from django.test import TestCase

from tasks.models import Tag, Task


class TagModelTest(TestCase):

    def test_tag_model_name(self):
        tag = Tag.objects.create(title="TestTag")
        self.assertEqual(str(tag), "TestTag")


class TaskModelTest(TestCase):

    def test_task_model_name(self):
        tag = Tag.objects.create(title="Testtag")
        task = Task.objects.create(
            content="TestTask",
            performance=True,
        )
        task.tags.add(tag)
        task.save()
        self.assertEqual(str(task), "TestTask")

from enum import unique

from django.db import models


class Tags(models.Model):
    title = models.CharField(max_length=255, unique=True)


class Tasks(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    marks = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags)

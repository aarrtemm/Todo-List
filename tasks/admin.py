from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("content", "performance")


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass

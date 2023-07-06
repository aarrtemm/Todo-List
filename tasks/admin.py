from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass

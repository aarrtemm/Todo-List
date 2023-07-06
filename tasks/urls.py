from django.urls import path

from tasks.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView
)

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
]

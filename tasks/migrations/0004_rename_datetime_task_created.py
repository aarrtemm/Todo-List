# Generated by Django 4.2.3 on 2023-07-05 10:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_alter_task_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="datetime",
            new_name="created",
        ),
    ]

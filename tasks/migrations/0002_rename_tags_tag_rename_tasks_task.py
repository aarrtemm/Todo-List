# Generated by Django 4.2.3 on 2023-07-05 10:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tags",
            new_name="Tag",
        ),
        migrations.RenameModel(
            old_name="Tasks",
            new_name="Task",
        ),
    ]

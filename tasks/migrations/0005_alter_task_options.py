# Generated by Django 4.2.3 on 2023-07-05 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_datetime_task_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-marks', 'created')},
        ),
    ]

# Generated by Django 5.1 on 2024-08-27 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='due_date',
        ),
    ]

# Generated by Django 5.1 on 2024-08-27 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subgoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Completed'), ('I', 'In Progress')], default='P', max_length=1)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='M', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgoals', to='subgoal.goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

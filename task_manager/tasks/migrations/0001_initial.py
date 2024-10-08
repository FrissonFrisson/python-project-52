# Generated by Django 5.1 on 2024-08-27 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '__first__'),
        ('statuses', '__first__'),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('description', models.TextField(verbose_name='Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks_created', to='users.customuser', verbose_name='Author')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks_executor', to='users.customuser', verbose_name='Executor')),
                ('labels', models.ManyToManyField(blank=True, to='labels.label', verbose_name='Labels')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.taskstatus', verbose_name='Status')),
            ],
        ),
    ]

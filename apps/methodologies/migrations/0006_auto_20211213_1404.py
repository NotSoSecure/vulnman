# Generated by Django 3.2.9 on 2021-12-13 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('methodologies', '0005_projectmethodology_projecttask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttask',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_projecttask_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='status',
            field=models.CharField(choices=[('todo', 'To Do'), ('progress', 'In Progress'), ('done', 'Done')], default='todo', max_length=28),
        ),
    ]

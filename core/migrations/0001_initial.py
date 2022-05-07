# Generated by Django 4.0.4 on 2022-04-17 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0004_alter_service_host'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_projectapitoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('task_id', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['-date_updated'],
                'unique_together': {('task_id',)},
            },
        ),
        migrations.CreateModel(
            name='TaskCondition',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('asset_type', models.CharField(choices=[('webapplication', 'Web Application'), ('webrequest', 'Web Request'), ('host', 'Host'), ('service', 'Service')], max_length=128)),
                ('condition', models.CharField(blank=True, max_length=256, null=True)),
                ('is_regex', models.BooleanField(default=False)),
                ('on_pentest', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
            options={
                'unique_together': {('task', 'asset_type', 'condition', 'is_regex')},
            },
        ),
        migrations.CreateModel(
            name='AssetTask',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Open'), (1, 'Closed'), (2, 'To Review'), (3, 'Not Tested'), (4, 'Not Applicable')], default=0)),
                ('asset_host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.host')),
                ('asset_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.service')),
                ('asset_webapp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.webapplication')),
                ('asset_webrequest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.webrequest')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
            options={
                'unique_together': {('task', 'project', 'asset_webapp'), ('task', 'project', 'asset_host'), ('task', 'project', 'asset_service'), ('task', 'project', 'asset_webrequest')},
            },
        ),
    ]
# Generated by Django 3.2.12 on 2022-02-23 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PentestReport',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('report_type', models.CharField(choices=[('draft', 'Draft'), ('release', 'Relase')], max_length=16)),
                ('raw_source', models.TextField(blank=True, null=True)),
                ('pdf_source', models.BinaryField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pentest_report_author', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('revision', models.CharField(default='0.1', help_text='The reports are ordered by revisions', max_length=6)),
                ('custom_title', models.CharField(blank=True, help_text='Overwrite Project Title', max_length=64, null=True)),
                ('changes', models.CharField(max_length=128)),
                ('raw_source', models.TextField(blank=True, null=True)),
                ('pdf_source', models.BinaryField(blank=True, null=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'ordering': ['revision'],
                'unique_together': {('project', 'revision')},
            },
        ),
        migrations.CreateModel(
            name='ReportShareToken',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('share_token', models.CharField(blank=True, max_length=512, null=True)),
                ('date_expires', models.DateTimeField()),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reporting.report')),
            ],
        ),
        migrations.CreateModel(
            name='ReportSection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('text', models.TextField(help_text='Markdown supported!')),
                ('order', models.IntegerField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.pentestreport')),
            ],
            options={
                'verbose_name': 'Report Section',
                'verbose_name_plural': 'Report Sections',
                'unique_together': {('report', 'order')},
            },
        ),
    ]

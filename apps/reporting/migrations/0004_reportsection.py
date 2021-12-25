# Generated by Django 3.2.9 on 2021-12-20 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commands', '0001_initial'),
        ('projects', '0006_auto_20211219_1518'),
        ('reporting', '0003_alter_reportsharetoken_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('text', models.TextField(help_text='Markdown supported!')),
                ('order', models.IntegerField()),
                ('command_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.report')),
            ],
            options={
                'verbose_name': 'Report Section',
                'verbose_name_plural': 'Report Sections',
                'unique_together': {('report', 'order'), ('project', 'name')},
            },
        ),
    ]
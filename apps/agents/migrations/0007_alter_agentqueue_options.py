# Generated by Django 3.2.9 on 2021-12-09 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0006_rename_agent_name_agent_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentqueue',
            options={'ordering': ['-date_updated']},
        ),
    ]
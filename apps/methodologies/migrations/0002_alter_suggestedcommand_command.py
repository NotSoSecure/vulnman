# Generated by Django 3.2.9 on 2021-12-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methodologies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestedcommand',
            name='command',
            field=models.TextField(help_text='The following placeholders are available: %target_ip%, %target_domain%, %target_port%, %target_scheme%'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methodologies', '0006_alter_taskcondition_asset_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcondition',
            name='asset_type',
            field=models.CharField(choices=[('webapplication', 'Web Application'), ('webrequest', 'Web Request'), ('host', 'Host'), ('service', 'Service')], max_length=128),
        ),
    ]
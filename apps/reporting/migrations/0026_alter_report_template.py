# Generated by Django 4.1.2 on 2022-12-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0025_alter_report_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='template',
            field=models.CharField(default='default', max_length=64),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_cvss_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontact',
            name='position',
            field=models.CharField(max_length=64),
        ),
    ]
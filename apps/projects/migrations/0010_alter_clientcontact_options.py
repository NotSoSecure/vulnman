# Generated by Django 3.2.9 on 2021-12-27 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_report_default_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientcontact',
            options={'verbose_name': 'Client Contact', 'verbose_name_plural': 'Client Contacts'},
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-06 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projectmember_role'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('project', 'email')},
        ),
    ]
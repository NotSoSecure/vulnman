# Generated by Django 3.2.9 on 2021-11-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0046_auto_20211129_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='webapplicationurlpath',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
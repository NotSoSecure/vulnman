# Generated by Django 4.0.4 on 2022-06-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0019_delete_vulnerabilityreference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
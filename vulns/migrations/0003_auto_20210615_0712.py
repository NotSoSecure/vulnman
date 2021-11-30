# Generated by Django 3.2.4 on 2021-06-15 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0002_vulnerability_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProofOfConcept',
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads/pocs'),
        ),
    ]
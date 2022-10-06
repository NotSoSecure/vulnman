# Generated by Django 4.1.2 on 2022-10-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0013_alter_owaspscore_skills_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owaspscore',
            name='motive',
            field=models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Low Or No Reward (1)'), (4, 'Possible Reward (4)'), (9, 'High Reward (9)')], help_text='How motivated is this group of threat agents to find and exploit this vulnerability?'),
        ),
        migrations.AlterField(
            model_name='owaspscore',
            name='opportunity',
            field=models.PositiveIntegerField(choices=[(0, 'Full access or expensive resources required (0)'), (4, 'Special access or resources required (4)'), (7, 'Some access or resources required (7)'), (9, 'No access or resources required (9)')], help_text='What resources and opportunities are required for this group of threat agents to find and exploit this vulnerability?'),
        ),
        migrations.AlterField(
            model_name='owaspscore',
            name='population_size',
            field=models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (2, 'System Administrators (2)'), (4, 'Intranet Users (4)'), (5, 'Partners (5)'), (6, 'Authenticated users (6)'), (9, 'Anonymous users (9)')], help_text='How large is this group of threat agents?'),
        ),
    ]

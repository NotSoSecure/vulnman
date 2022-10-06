# Generated by Django 4.1.2 on 2022-10-06 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_projectcontact_unique_together'),
        ('findings', '0011_vulnerability_date_retested'),
    ]

    operations = [
        migrations.CreateModel(
            name='OWASPScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_required', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Security Penetration Skills (1)'), (3, 'Networking And Programming Skills (3)'), (4, 'Advanced Computer User (4)'), (6, 'Some Technical Skills (6)'), (9, 'No Technical Skills (9)')])),
                ('motive', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Low Or No Reward (1)'), (4, 'Possible Reward (4)'), (9, 'High Reward (9)')])),
                ('opportunity', models.PositiveIntegerField(choices=[(0, 'Full access or expensive resources required (0)'), (4, 'Special access or resources required (4)'), (7, 'Some access or resources required (7)'), (9, 'No access or resources required (9)')])),
                ('population_size', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (2, 'System Administrators (2)'), (4, 'Intranet Users (4)'), (5, 'Partners (5)'), (6, 'Authenticated users (6)'), (9, 'Anonymous users (9)')])),
                ('ease_of_discovery', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Practically impossible (1)'), (3, 'Difficult (3)'), (7, 'Easy (7)'), (9, 'Automated Tools Available (9)')])),
                ('ease_of_exploit', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Theoretical (1)'), (3, 'Difficult (3)'), (5, 'Easy (5)'), (9, 'Automated Tools Available (9)')])),
                ('awareness', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Unknown (1)'), (4, 'Hidden (4)'), (6, 'Obvious (6)'), (9, 'Public Knowledge (9)')])),
                ('intrusion_detection', models.PositiveIntegerField(choices=[(0, 'Not Applicable (0)'), (1, 'Active detection in application (1)'), (3, 'Logged and reviewed (3)'), (8, 'Logged without review (8)'), (9, 'Not logged (9)')])),
                ('loss_of_confidentiality', models.PositiveIntegerField(choices=[(2, 'Minimal non-sensitive data disclosed (2)'), (6, 'Minimal critical data disclosed (6)'), (6, 'Extensive non-sensitive data disclosed (6)'), (7, 'Extensive critical data disclosed (7)'), (9, 'All data disclosed (9)')])),
                ('loss_of_integrity', models.PositiveIntegerField(choices=[(1, 'Minimal slightly corrupt data (1)'), (3, 'Minimal seriously corrupt data (3)'), (5, 'Extensive slightly corrupt data (5)'), (7, 'Extensive seriously corrupt data (7)'), (9, 'All data totally corrupt (9)')])),
                ('loss_of_availability', models.PositiveIntegerField(choices=[(1, 'Minimal secondary services interrupted (1)'), (5, 'Minimal primary services interrupted (5)'), (5, 'Extensive secondary services interrupted (5)'), (7, 'Extensive primary services interrupted (7)'), (9, 'All services completely list (9)')])),
                ('loss_of_accountability', models.PositiveIntegerField(choices=[(1, 'Fully traceable (1)'), (7, 'Possibly traceable (7)'), (9, 'Completely anonymous (9)')])),
                ('financial_damage', models.PositiveIntegerField(choices=[(1, 'Less than the cost to fix the vulnerability (1)'), (3, 'Minor effect on annual profit (3)'), (7, 'Significant effect on annual profit (7)'), (9, 'Bankruptcy (9)')], help_text='How much financial damage will result from an exploit?')),
                ('reputation_damage', models.PositiveIntegerField(choices=[(1, 'Minimal damage (1)'), (4, 'Loss of major accounts (4)'), (5, 'Loss of goodwill (5)'), (9, 'Brand damage (9)')], help_text='Would an exploit result in reputation damage that would harm the business?')),
                ('non_compliance', models.PositiveIntegerField(choices=[(2, 'Minor violation (2)'), (5, 'Clear violation (5)'), (7, 'High profile violation (7)')], help_text='How much exposure does non-compliance introduce?')),
                ('privacy_violation', models.PositiveIntegerField(choices=[(3, 'One individual (3)'), (5, 'Hundreds of people (5)'), (7, 'Thousands of people (7)'), (9, 'Millions of people (9)')], help_text='How much personally identifiable information could be disclosed?')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('vulnerability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='findings.vulnerability')),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-06 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_projectcontact_unique_together'),
        ('findings', '0016_remove_vulnerability_cvss_a_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVSScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_vector', models.CharField(blank=True, choices=[('N', 'Network (N)'), ('P', 'Physical (P)'), ('A', 'Adjacent (A)')], max_length=3, null=True)),
                ('attack_complexity', models.CharField(blank=True, choices=[('L', 'Low (L)'), ('H', 'High (H)')], max_length=3, null=True)),
                ('privilege_required', models.CharField(blank=True, choices=[('N', 'None (N)'), ('L', 'Low (L)'), ('H', 'High (H)')], max_length=3, null=True)),
                ('user_interaction', models.CharField(blank=True, choices=[('N', 'None (N)'), ('R', 'Required (R)')], max_length=3, null=True)),
                ('scope', models.CharField(blank=True, choices=[('U', 'Unchanged (U)'), ('C', 'Changed (C)')], max_length=3, null=True)),
                ('confidentiality', models.CharField(blank=True, choices=[('N', 'None (N)'), ('L', 'Low (L)'), ('H', 'High (H)')], max_length=3, null=True)),
                ('integrity', models.CharField(blank=True, choices=[('N', 'None (N)'), ('L', 'Low (L)'), ('H', 'High (H)')], max_length=3, null=True)),
                ('availability', models.CharField(blank=True, choices=[('N', 'None (N)'), ('L', 'Low (L)'), ('H', 'High (H)')], max_length=3, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('vulnerability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='findings.vulnerability')),
            ],
        ),
    ]

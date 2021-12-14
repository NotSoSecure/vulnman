# Generated by Django 3.2.9 on 2021-12-14 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0004_commandhistoryitem_command_created'),
        ('networking', '0005_alter_hostname_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='command_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem'),
        ),
        migrations.AddField(
            model_name='hostname',
            name='command_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem'),
        ),
        migrations.AddField(
            model_name='service',
            name='command_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem'),
        ),
    ]
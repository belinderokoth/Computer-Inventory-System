# Generated by Django 4.2.5 on 2023-10-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_computer_computer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='operating_system',
            field=models.CharField(blank=True, choices=[('Windows 10', 'Windows 10'), ('Windows 8', 'Windows 8'), ('Linux', 'Linux')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='users_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_operating_system_alter_computer_operating_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
    ]

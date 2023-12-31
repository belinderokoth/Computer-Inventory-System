# Generated by Django 4.2.5 on 2023-10-05 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_computer_operating_system_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='operating_system',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='computer',
            name='operating_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.operating_system'),
        ),
    ]

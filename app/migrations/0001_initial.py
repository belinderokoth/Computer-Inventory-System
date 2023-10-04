# Generated by Django 4.2.5 on 2023-10-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(max_length=30)),
                ('IP_address', models.CharField(max_length=30)),
                ('MAC_address', models.CharField(max_length=30)),
                ('users_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase Date (mm/dd/yyyy)')),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

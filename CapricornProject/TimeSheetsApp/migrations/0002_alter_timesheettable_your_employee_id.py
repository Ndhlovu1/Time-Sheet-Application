# Generated by Django 4.1.7 on 2023-02-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheetsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheettable',
            name='your_employee_Id',
            field=models.SmallIntegerField(default=10),
        ),
    ]
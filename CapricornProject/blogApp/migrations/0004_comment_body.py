# Generated by Django 4.1.7 on 2023-03-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenzApp', '0007_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='terms',
            field=models.BooleanField(default=False),
        ),
    ]

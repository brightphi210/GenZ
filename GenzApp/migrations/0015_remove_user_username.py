# Generated by Django 4.2.6 on 2023-11-15 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GenzApp', '0014_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

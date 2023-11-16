# Generated by Django 4.1.3 on 2023-07-19 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GenzApp', '0005_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='news_pics/')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('intro', models.TextField()),
                ('body', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GenzApp.authors')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GenzApp.category')),
            ],
        ),
    ]

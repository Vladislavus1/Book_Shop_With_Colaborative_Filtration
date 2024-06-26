# Generated by Django 5.0.4 on 2024-06-15 07:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=500)),
                ('book_image', models.URLField(max_length=500)),
                ('book_price', models.CharField(max_length=500)),
                ('book_author', models.CharField(max_length=500)),
                ('book_genre', models.CharField(max_length=500)),
                ('book_url', models.URLField(max_length=500)),
                ('views', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('user_key', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('detectives_count', models.IntegerField(default=0)),
                ('fighters_count', models.IntegerField(default=0)),
                ('thrillers_count', models.IntegerField(default=0)),
                ('romantics_count', models.IntegerField(default=0)),
                ('fantasy_count', models.IntegerField(default=0)),
            ],
        ),
    ]

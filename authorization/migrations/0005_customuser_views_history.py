# Generated by Django 5.0.4 on 2024-06-20 11:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_alter_customuser_search_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='views_history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=''), default=list, size=None),
        ),
    ]

# Generated by Django 5.0.4 on 2024-06-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='detectives_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='fantasy_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='fighters_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='romantics_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='thrillers_count',
            field=models.IntegerField(),
        ),
    ]

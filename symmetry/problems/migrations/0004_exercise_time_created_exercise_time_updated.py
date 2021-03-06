# Generated by Django 4.0.2 on 2022-02-18 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_exercise_html_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='time_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

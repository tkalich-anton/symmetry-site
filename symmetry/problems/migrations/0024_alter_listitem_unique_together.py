# Generated by Django 4.0.3 on 2022-03-05 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0023_rename_time_created_problem_created_at_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='listitem',
            unique_together={('problem', 'list')},
        ),
    ]

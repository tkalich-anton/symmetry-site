# Generated by Django 4.0.2 on 2022-02-21 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0008_remove_exercise_branch_theme_branch'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exercise',
            new_name='Problem',
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-04 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0018_list_problems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='lists',
        ),
    ]

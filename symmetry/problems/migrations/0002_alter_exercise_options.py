# Generated by Django 4.0.2 on 2022-02-17 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
    ]

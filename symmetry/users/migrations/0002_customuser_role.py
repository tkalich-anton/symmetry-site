# Generated by Django 4.0.8 on 2022-11-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Роль'),
        ),
    ]

# Generated by Django 4.0.8 on 2022-11-20 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listmanager', '0004_alter_item_child_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='multi_items',
        ),
        migrations.AddField(
            model_name='item',
            name='multi_items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='multiitems', to='listmanager.multiitem', verbose_name='Массив мульти элементов'),
            preserve_default=False,
        ),
    ]

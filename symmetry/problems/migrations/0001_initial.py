# Generated by Django 4.0.8 on 2022-11-27 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import problems.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Раздел')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='Флаг')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='problems.branch', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='ProblemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип')),
                ('condition', models.CharField(max_length=100, null=True, verbose_name='Условие')),
            ],
            options={
                'verbose_name': 'Тип задания',
                'verbose_name_plural': 'Типы заданий',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Источник',
                'verbose_name_plural': 'Источники',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('published', 'Опубликовано'), ('not_published', 'Не опубликовано')], default='not_published', max_length=15, verbose_name='Статус')),
                ('body', models.TextField(verbose_name='Условие')),
                ('answer', models.TextField(blank=True, max_length=50, verbose_name='Ответ')),
                ('prompt', models.TextField(blank=True, verbose_name='Подсказка')),
                ('solution', models.TextField(blank=True, verbose_name='Решение')),
                ('open_solution', models.BooleanField(default=False, verbose_name='Открытое решение')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('complexity', models.IntegerField(default=1, null=True, verbose_name='Сложность')),
                ('analogs', models.ManyToManyField(blank=True, to='problems.problem', verbose_name='Аналоги')),
                ('author', models.ForeignKey(default=problems.models.Author.get_default_pk, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='author', to='problems.author', verbose_name='Автор')),
                ('branch', mptt.fields.TreeForeignKey(default=problems.models.Branch.get_default_pk, limit_choices_to={'children__isnull': True}, on_delete=django.db.models.deletion.SET_DEFAULT, to='problems.branch', verbose_name='Раздел')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('example', models.ForeignKey(blank=True, limit_choices_to={'open_solution': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.problem', verbose_name='Пример')),
                ('problemtype', models.ForeignKey(blank=True, default=problems.models.ProblemType.get_default_pk, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='problems.problemtype', verbose_name='Тип задания')),
                ('source', models.ForeignKey(default=problems.models.Source.get_default_pk, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='source', to='problems.source', verbose_name='Источник')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]

from django.db import models
from django.urls import reverse

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class StatusChoices(models.TextChoices):
    PUBLISHED = 'published', 'Опубликовано'
    NOT_PUBLISHED = 'not_published', 'Не опубликовано'


class Branch(MPTTModel):
    title = models.CharField('Раздел', max_length=50, db_index=True)
    slug = models.SlugField('Метка', unique=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def get_absolute_url(self):
        return reverse('branch', kwargs={'slug': self.slug})

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(title="Без Раздела", slug="no_branch")
        return obj.pk


class List(models.Model):
    status = models.CharField(
        'Статус',
        max_length=15,
        default=StatusChoices.NOT_PUBLISHED,
        choices=StatusChoices.choices
    )

    class Meta:
        verbose_name = 'Список заданий'
        verbose_name_plural = 'Списки заданий'

    def __str__(self):
        return f"Список  {self.pk}"


class ListItem(models.Model):
    problem = models.ForeignKey(
        'Problem',
        on_delete=models.PROTECT,
        limit_choices_to={'status': 'published'},
        verbose_name='Задание',
        related_name='problem_item'
    )
    list = models.ForeignKey(
        'List',
        on_delete=models.CASCADE,
        verbose_name='Список',
        related_name='list'
    )

    class Meta:
        verbose_name = 'Элемент Списка'
        verbose_name_plural = 'Элементы Списков'
        unique_together = (('problem', 'list'),)

    def __str__(self):
        return f"{self.problem} | {self.list}"


class Problem(models.Model):
    status = models.CharField(
        'Статус',
        max_length=15,
        default=StatusChoices.NOT_PUBLISHED,
        choices=StatusChoices.choices
    )
    condition = models.TextField('Условие')
    branch = TreeForeignKey('Branch', on_delete=models.SET_DEFAULT, verbose_name='Раздел',
                            default=Branch.get_default_pk)
    answer = models.TextField('Ответ', max_length=50, null=True, blank=True)
    solution = models.TextField('Решение', null=True, blank=True)
    note = models.TextField('Примечание', null=True, blank=True)
    complexity = models.IntegerField('Сложность', null=True, blank=True)
    source = models.ForeignKey('Source', on_delete=models.PROTECT, null=True, verbose_name='Источник', blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, verbose_name='Автор', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Задание {self.id}"

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def get_absolute_url(self):
        return reverse('problem', kwargs={'pk': self.pk})


class Source(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class Author(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

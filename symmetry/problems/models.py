from django.db import models
from django.urls import reverse


# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

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


class Theme(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def get_absolute_url(self):
        return reverse('theme_by_branch', kwargs={'slug': self.slug})


class Problem(models.Model):
    condition = models.TextField('Условие')
    branch = TreeForeignKey('Branch', on_delete=models.PROTECT, verbose_name='Раздел', null=True)
    answer = models.TextField('Ответ', max_length=50, null=True, blank=True)
    solution = models.TextField('Решение', null=True, blank=True)
    note = models.TextField('Примечание', null=True, blank=True)
    complexity = models.IntegerField('Сложность', null=True, blank=True)
    source = models.ForeignKey('Source', on_delete=models.PROTECT, null=True, verbose_name='Источник', blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, verbose_name='Автор', blank=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

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
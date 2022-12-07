from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel

from listmanager.models import MultiItem
from mixins.models import CommonModel
from users.models import CustomUser


class CategoryManager(TreeManager):
    def viewable(self, level):
        queryset = self.get_queryset().filter(level=level)
        return queryset

class StatusChoices(models.TextChoices):
    PUBLISHED = 'published', 'Опубликовано'
    NOT_PUBLISHED = 'not_published', 'Не опубликовано'


class Branch(MPTTModel):
    title = models.CharField('Раздел', max_length=50, db_index=True)
    slug = models.SlugField('Флаг', unique=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    objects = CategoryManager()

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


class Source(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(title="Нет Источника")
        return obj.pk


class Author(models.Model):
    title = models.CharField('Имя', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(title="Нет Автора")
        return obj.pk


class ProblemType(models.Model):
    title = models.CharField('Тип', max_length=100)
    condition = models.CharField('Условие', max_length=100, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип задания'
        verbose_name_plural = 'Типы заданий'

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(title="Без Типа")
        return obj.pk


class Problem(CommonModel):

    status = models.CharField(
        'Статус',
        max_length=15,
        default=StatusChoices.NOT_PUBLISHED,
        choices=StatusChoices.choices
    )
    problemtype = models.ForeignKey(
        'ProblemType',
        on_delete=models.SET_DEFAULT,
        default=ProblemType.get_default_pk,
        null=True,
        blank=True,
        verbose_name='Тип задания'
    )
    body = models.TextField('Условие')
    branch = TreeForeignKey(
        'Branch',
        on_delete=models.SET_DEFAULT,
        default=Branch.get_default_pk,
        verbose_name='Раздел',
        limit_choices_to={'children__isnull': True}
    )
    answer = models.TextField(
        'Ответ',
        max_length=50,
        blank=True
    )
    prompt = models.TextField(
        'Подсказка',
        blank=True
    )
    solution = models.TextField(
        'Решение',
        blank=True
    )
    open_solution = models.BooleanField(
        'Открытое решение',
        default=False
    )
    note = models.TextField(
        'Примечание',
        blank=True
    )
    analogs = models.ManyToManyField(
        'self',
        verbose_name='Аналоги',
        blank=True
    )
    example = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Пример',
        blank=True, null=True,
        limit_choices_to={'open_solution': True},
    )
    complexity = models.IntegerField(
        'Сложность',
        null=True,
        default=1
    )
    source = models.ForeignKey(
        'Source',
        on_delete=models.SET_DEFAULT,
        default=Source.get_default_pk,
        verbose_name='Источник',
        related_name="source"
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_DEFAULT,
        default=Author.get_default_pk,
        related_name="author",
        verbose_name='Автор'
    )

    def __str__(self):
        return f"Задание {self.id}"

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def get_absolute_url(self):
        return reverse('problem', kwargs={'pk': self.pk})

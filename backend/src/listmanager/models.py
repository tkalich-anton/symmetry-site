from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mixins.models import CommonModel


class StatusChoices(models.TextChoices):
    PUBLISHED = 'published', 'Опубликовано'
    NOT_PUBLISHED = 'not_published', 'Не опубликовано'


class List(CommonModel):
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


class MultiItem(models.Model):
    condition = models.CharField('Условие', max_length=100, blank=False)
    columns = models.IntegerField('Кол-во колонок', default=1)

    class Meta:
        verbose_name = 'Мульти элемент списка'
        verbose_name_plural = 'Мульти элементы списков'

    def __str__(self):
        return f"Мульти элемент #{self.id}"


class Item(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    item_number = models.IntegerField('Порядковый номер', default=None, null=True)
    is_active = models.BooleanField('Активен', default=True)
    is_multi_item = models.BooleanField('Мульти элемент', default=False)
    is_child = models.BooleanField('Подзадание', default=False)
    child_number = models.IntegerField('Порядковый номер подзадания', default=None, blank=True, null=True)
    list = models.ForeignKey(
        'List',
        on_delete=models.CASCADE,
        verbose_name='Список',
        related_name='list'
    )
    multi_items = models.ForeignKey(
        'MultiItem',
        on_delete=models.CASCADE,
        verbose_name='В мультемассиве',
        related_name='multiitems',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Элемент Списка'
        verbose_name_plural = 'Элементы Списков'

    def __str__(self):
        return f"Элемент #{self.id} из {self.list}"

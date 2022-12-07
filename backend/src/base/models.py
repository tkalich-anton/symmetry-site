from django.db import models


class PublishOption(models.Model):
    status = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(title="Не опубликовано")
        return obj.pk
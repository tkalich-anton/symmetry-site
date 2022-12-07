from django.db import models


class Statement(models.Model):
    title = models.CharField('Название', max_length=300, blank=True)
    body = models.TextField('Содержание', blank=True)
    is_true = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Definition(Statement):
    class Meta:
        verbose_name = 'Определение'
        verbose_name_plural = 'Определения'


class Theorem(Statement):
    reverse_theorem = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    reverse_is_true = models.BooleanField(default=None)
    proof = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Теорема'
        verbose_name_plural = 'Теоремы'
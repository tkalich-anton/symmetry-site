from django.conf import settings
from django.db import models

from users.models import CustomUser


class CommonModel(models.Model):
    """Common fields that are shared among all models."""

    created_by = models.ForeignKey(CustomUser,
                                   editable=False,
                                   related_name="+",
                                   on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(CustomUser,
                                   editable=False,
                                   related_name="+",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      editable=False)

    class Meta:
        abstract = True

from django.contrib import admin

from base.models import PublishOption


@admin.register(PublishOption)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'id')
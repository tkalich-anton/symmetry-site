from django.contrib import admin

from academy.models import Definition, Theorem


@admin.register(Definition)
class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)


@admin.register(Theorem)
class TheoremAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
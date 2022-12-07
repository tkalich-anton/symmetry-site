from django.contrib import admin
from .models import List, Item, MultiItem


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ('__str__', 'status')


@admin.register(Item)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'content_type', 'object_id', 'content_object')


@admin.register(MultiItem)
class MultiItemAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ('__str__',)


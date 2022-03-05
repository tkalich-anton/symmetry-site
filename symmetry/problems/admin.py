from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from .models import Problem, Branch, Source, Author, List, ListItem

admin.site.register(Source)
admin.site.register(Author)
admin.site.register(Branch)

class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 0

@admin.register(List)
class ListAdmin(admin.ModelAdmin, DynamicArrayMixin):
    inlines = [ListItemInline]
    list_display = ('__str__', 'status')

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'branch', 'status')

@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    pass


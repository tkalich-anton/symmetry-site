from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Problem, Branch, Source, Author

# Register your models here.

admin.site.register(Problem)
admin.site.register(Source)
admin.site.register(Author)

class ThemeAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Branch, ThemeAdmin)

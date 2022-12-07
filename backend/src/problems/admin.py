from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Problem, Branch, Source, ProblemType, Author


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'problemtype', 'status')
    actions_on_top = True


@admin.register(Branch)
class BranchAdmin(DjangoMpttAdmin):
    list_display = ['title', 'id', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')

@admin.register(ProblemType)
class ProblemTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'condition', 'id')


from django import forms
from mptt.forms import TreeNodeChoiceField

from .models import Branch

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['title']
    category = TreeNodeChoiceField(queryset=Branch.objects.all(), label='')
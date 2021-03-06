from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Problem, Branch, List, ListItem


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'problems/index.html', context=context)

class BranchList(ListView):
    model = Branch
    context_object_name = 'childs'
    template_name = 'problems/branch_list.html'

    def get_queryset(self):
        if self.kwargs:
            branch = Branch.objects.get(slug=self.kwargs['slug'])
            queryset = Branch.objects.filter(parent_id=branch.id)
        else:
            queryset = Branch.objects.filter(level=0)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs:
            branch = Branch.objects.get(slug=self.kwargs['slug'])
            context['branch'] = branch
            if branch.is_leaf_node():
                problems = Problem.objects.filter(branch=branch)
                context['problems'] = problems
        else:
            context['title'] = 'Разделы'
        return context

class SingleProblem(DetailView):
    model = Problem
    context_object_name = 'problem'
    template_name = 'problems/problem.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SingleList(DetailView):
    model = List
    context_object_name = 'list'
    template_name = 'problems/list.html'
    def get_context_data(self, **kwargs):
        queryset = Problem.objects.filter(problem_item__list__pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['problems'] = queryset
        return context



def about(request):
    return render(request, 'problems/about.html')
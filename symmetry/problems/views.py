from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mptt.forms import TreeNodeChoiceField
from mptt.managers import TreeManager
from rest_flex_fields import is_expanded
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from mixins.views import CommonViewSet
from users.models import CustomUser
from .models import Problem, Branch, ProblemType, Source, Author
from .serializers import ProblemTypeSerializer, ProblemSerializer, BranchSerializer, AuthorSerializer, SourceSerializer


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'problems/index.html', context=context)

# class BranchList(ListView):
#     model = Branch
#     context_object_name = 'childs'
#     template_name = 'problems/branch_list.html'
#
#     def get_queryset(self):
#         if self.kwargs:
#             branch = Branch.objects.get(slug=self.kwargs['slug'])
#             queryset = Branch.objects.filter(parent_id=branch.id)
#         else:
#             queryset = Branch.objects.filter(level=0)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.kwargs:
#             branch = Branch.objects.get(slug=self.kwargs['slug'])
#             context['branch'] = branch
#             if branch.is_leaf_node():
#                 problems = Problem.objects.filter(branch=branch)
#                 context['problems'] = problems
#         else:
#             context['title'] = 'Разделы'
#         return context



def about(request):
    return render(request, 'problems/about.html')


class ProblemTypeViewSet(ModelViewSet):
    queryset = ProblemType.objects.all()
    serializer_class = ProblemTypeSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ProblemViewSet(CommonViewSet, FlexFieldsMixin):
    serializer_class = ProblemSerializer
    permission_classes = (IsAuthenticated,)
    permit_list_expands = ['branch', 'branch.parent', 'problemtype', 'author', 'source']
    filterset_fields = ('branch',)

    def get_queryset(self):
        queryset = Problem.objects.all()
        if is_expanded(self.request, 'branch'):
            queryset = queryset.prefetch_related('branch')

        if is_expanded(self.request, 'problemtype'):
            queryset = queryset.prefetch_related('problemtype')

        if is_expanded(self.request, 'author'):
            queryset = queryset.prefetch_related('author')

        if is_expanded(self.request, 'source'):
            queryset = queryset.prefetch_related('source')

        return queryset

    def update(self, request, *args, **kwargs):
        problem = self.get_object()
        data = request.data

        problem_type = ProblemType.objects.get(id=data["problemtype"])
        problem_branch = Branch.objects.get(id=data["branch"])
        problem_example = Problem.objects.get(id=data["example"])
        problem_source = Source.objects.get(id=data["source"])
        problem_author = Author.objects.get(id=data["author"])


        problem.problemtype = problem_type
        problem.branch = problem_branch
        problem.example = problem_example
        problem.source = problem_source
        problem.author = problem_author

        problem.status = data["status"]
        problem.body = data["body"]
        problem.answer = data["answer"]
        problem.prompt = data["prompt"]
        problem.solution = data["solution"]
        problem.open_solution = data["open_solution"]
        problem.note = data["note"]
        problem.complexity = data["complexity"]

        problem.save()


        serializer = ProblemSerializer(problem)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        problem = self.get_object()
        data = request.data
        user = CustomUser(self.request.user)

        try:
            problem_type = ProblemType.objects.get(id=data["problemtype"])
            problem.problemtype = problem_type
        except KeyError:
            pass

        try:
            problem_branch = Branch.objects.get(id=data["branch"])
            problem.branch = problem_branch
        except KeyError:
            pass

        try:
            problem_example = Problem.objects.get(id=data["example"])
            problem.example = problem_example
        except Problem.DoesNotExist:
            pass
        except KeyError:
            pass

        try:
            problem_source = Source.objects.get(id=data["source"])
            problem.source = problem_source
        except Source.DoesNotExist:
            pass
        except KeyError:
            pass

        try:
            problem_author = Author.objects.get(id=data["author"])
            problem.author = problem_author
        except Author.DoesNotExist:
            pass
        except KeyError:
            pass

        problem.status = data.get("status", problem.status)
        problem.body = data.get("body", problem.body)
        problem.answer = data.get("answer", problem.answer)
        problem.prompt = data.get("prompt", problem.prompt)
        problem.solution = data.get("solution", problem.solution)
        problem.open_solution = data.get("open_solution", problem.open_solution)
        problem.note = data.get("note", problem.note)
        problem.complexity = data.get("complexity", problem.complexity)
        problem.updated_by = user.id

        problem.save()

        serializer = ProblemSerializer(problem)

        return Response(serializer.data)


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()

    serializer_class = BranchSerializer

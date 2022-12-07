from rest_framework.permissions import IsAuthenticated

from mixins.serializers import CommonSerializer
from mixins.views import CommonViewSet
from .models import List, Item
from rest_framework import viewsets
from .serializers import ListProblemSerializer, ItemSerializer



# class SingleList(DetailView):
#     model = List
#     context_object_name = 'list'
#     template_name = 'problems/list.html'
#
#     def get_context_data(self, **kwargs):
#         queryset = Problem.objects.filter(problem_item__list__pk=self.kwargs['pk'])
#         context = super().get_context_data(**kwargs)
#         context['problems'] = queryset
#         return context


class ListViewSet(CommonViewSet):
    queryset = List.objects.all()
    serializer_class = ListProblemSerializer
    permission_classes = [IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




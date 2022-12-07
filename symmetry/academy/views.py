from rest_framework.viewsets import ModelViewSet

from academy.models import Definition, Theorem
from academy.serializers import DefinitionSerializer, TheoremSerializer


class DefinitionViewSet(ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer


class TheoremViewSet(ModelViewSet):
    queryset = Theorem.objects.all()
    serializer_class = TheoremSerializer
from django.urls import path, re_path, include

from listmanager.views import ListViewSet
from .views import ProblemTypeViewSet, ProblemViewSet, BranchViewSet, AuthorViewSet, SourceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('problems', ProblemViewSet, basename='Problem')
router.register('problemtypes', ProblemTypeViewSet)
router.register('authors', AuthorViewSet)
router.register('sources', SourceViewSet)
router.register('branches', BranchViewSet)
router.register('lists', ListViewSet)

urlpatterns = []

urlpatterns += router.urls

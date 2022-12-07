from django.urls import path, re_path, include
from .views import DefinitionViewSet, TheoremViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('definitions', DefinitionViewSet)
router.register('theorems', TheoremViewSet)

urlpatterns = []

urlpatterns += router.urls
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('branches/', BranchList.as_view(), name='branches'),
    re_path(r'^branch/(?P<slug>.+)/$', BranchList.as_view(), name='branch'),
    path('problem/<int:pk>/', SingleProblem.as_view(), name='problem'),
]
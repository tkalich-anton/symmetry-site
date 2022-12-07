from django.contrib import admin
from django.urls import path, include

from users.views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    # gets all user profiles and create a new profile
    path("profiles", UserProfileListCreateView.as_view(), name="profiles"),
    # retrieves profile details of the currently logged in user
    path("profiles/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
]
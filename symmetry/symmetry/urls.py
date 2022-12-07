from django.contrib import admin
from django.urls import path, include

from users.views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('problems.urls')),
    path('api/', include('listmanager.urls')),
    path('api/', include('academy.urls')),
    path('auth/jwt/token/', MyTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api/", include("users.urls"))
]

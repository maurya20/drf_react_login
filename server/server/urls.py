from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('mysite.urls')),
    path("api/auth/", include('rest_auth.urls')),
    path("api/token/", obtain_jwt_token),   # For login getting JWT
   
]
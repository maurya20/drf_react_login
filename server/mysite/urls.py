from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from mysite.views import UserViewSet
from rest_framework import views
from .views import SignupView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('user_signup/',SignupView.as_view()),
        
]





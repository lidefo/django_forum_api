from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('profile', views.UserViewSet, basename='profile')
router.register('login', views.LoginViewSet, basename='login')


urlpatterns = [
    path('', include(router.urls))
]
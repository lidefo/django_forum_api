from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('profiles', views.UserViewSet, basename='profile')
router.register('login', views.LoginViewSet, basename='login')
router.register('topics', views.TopicViewSet)
router.register('messages', views.MessageViewSet)


urlpatterns = [
    path('', include(router.urls))
]
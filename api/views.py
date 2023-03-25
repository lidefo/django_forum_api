from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.utils import CustomObtainAuthToken
from .serializers import UserSerializer, TopicSerializer, MessageSerializer
from .permissions import UpdateOwnProfile, IsAuthorOrNot
from topics.models import Topic, Message
# Create your views here.

UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    '''Creating and updating profiles.'''
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)


class LoginViewSet(viewsets.ModelViewSet):
    '''Checks email and password and returns an auth token.'''
    queryset = UserModel.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        return CustomObtainAuthToken().as_view()(request=request._request)


class TopicViewSet(viewsets.ModelViewSet):
    '''Creating, deleting and updating topics.'''
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrNot, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    '''Creating, deleting and updating messages.'''
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrNot, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

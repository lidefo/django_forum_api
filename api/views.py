from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserSerializer
from .permissions import UpdateOwnProfile

# Create your views here.


UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)


class LoginViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        return ObtainAuthToken().as_view()(request=request._request)

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer
from .permissions import UpdateOwnProfile

# Create your views here.


UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
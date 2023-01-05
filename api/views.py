from django.contrib.auth import get_user_model
from rest_framework import viewsets


from .serializers import UserSerializer
from . import permissions

# Create your views here.


UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
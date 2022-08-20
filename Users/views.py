from rest_framework import viewsets
from Users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

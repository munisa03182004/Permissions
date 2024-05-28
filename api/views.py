from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from app_main.models import Note
from .serializers import NoteSerializer, UserSerializer

User = get_user_model()


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

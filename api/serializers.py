from rest_framework import serializers

from app_main.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'body', 'created', 'updated']


class UserSerializer(serializers.ModelField):
    ...

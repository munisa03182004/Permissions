from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from app_main.models import Note
from .serializers import NoteSerializer


User = get_user_model()


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()  # QuerySet[<Note object>, ...]
    serialized_data = NoteSerializer(instance=notes, many=True)
    return Response(data=serialized_data.data)


@api_view(['POST'])
def create_note(request):
    if request.method == 'POST':
        owner_id = request.data['owner']
        title = request.data['title']
        body = request.data['body']

        user = User.objects.get(id=owner_id)
        note = Note.objects.create(owner=user, title=title, body=body)
        note.save()
        return Response(data="Created", status=status.HTTP_201_CREATED)

    return Response()

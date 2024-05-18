from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.get_notes),  # localhost:8000/api/notes/
    path('notes/new/', views.create_note),
]

from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.get_notes),  # localhost:8000/api/notes/
    path('users/', views.get_users),  # localhost:8000/api/users/
    path('notes/new/', views.create_note),
]

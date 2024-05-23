from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/api/notes/
    path('notes/', views.notes),
    # localhost:8000/api/notes/edit/:id
    path('notes/<uuid:id>/', views.note),

    # localhost:8000/api/users/
    path('users/', views.UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    # localhost:8000/api/users/:pk
    path('users/<int:pk>/', views.UserViewSet.as_view({
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy',
    })),
]

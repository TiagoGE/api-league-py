from django.urls import path
from .views import UserCreateView, TeamCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('create-team/', TeamCreateView.as_view(), name='team-create'),
]

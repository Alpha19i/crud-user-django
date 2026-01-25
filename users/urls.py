from django.urls import path
from .views import users_create

urlpatterns = [
    path('create/', users_create),
]

from django.urls import path
from .views import home, users_list, users_create

urlpatterns = [
    path('', home),
    path('users/', users_list),
    path('users/create/', users_create),
]

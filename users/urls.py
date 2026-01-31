from django.urls import path
from .views import users_list, users_create, users_detail, users_update, users_delete

urlpatterns = [
    path('', users_list, name='users_list'),
    path('create/', users_create, name='users_create'),
    path('<int:id>/', users_detail, name='users_detail'),
    path('<int:id>/update/', users_update, name='users_update'),
    path('<int:id>/delete/', users_delete, name='users_delete'),
]

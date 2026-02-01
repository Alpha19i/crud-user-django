from django.shortcuts import render
from users.models import User

def home(request):
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    context = {
        'total_users': total_users,
        'active_users': active_users,
    }
    return render(request, 'home.html', context)

def users_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

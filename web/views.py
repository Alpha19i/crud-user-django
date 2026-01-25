from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def users_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

def users_create(request):
    if request.method == 'POST':
        User.objects.create(
            username=request.POST['username'],
            email=request.POST['email']
        )
        return redirect('/users/')
    return render(request, 'users/create.html')

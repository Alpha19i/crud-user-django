from django.shortcuts import render, redirect
from .forms import UserForm

def users_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = UserForm()

    return render(request, 'users/create.html', {'form': form})

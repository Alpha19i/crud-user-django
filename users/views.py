from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm
from .models import User

def users_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

def users_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('users_list')
    else:
        form = UserForm()

    return render(request, 'users/create.html', {'form': form})

def users_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'users/detail.html', {'user': user})

def users_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('users_detail', id=user.id)
    else:
        form = UserForm(instance=user)

    return render(request, 'users/update.html', {'form': form, 'user': user})

def users_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuário deletado com sucesso!')
        return redirect('users_list')

    return render(request, 'users/delete.html', {'user': user})

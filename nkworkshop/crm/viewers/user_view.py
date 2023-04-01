from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
# only superuser can access this page
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

# def user_detail(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     return render(request, 'user/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user/user_form.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user/user_confirm_delete.html', {'user': user})
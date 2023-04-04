
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from ..forms import MessageForm
from ..models import Action


def message_create(request):
    action_id = None
    if request.GET.get('action_id'):
        action_id = request.GET.get('action_id', None)
        action = Action.objects.get(pk=action_id)
        form = MessageForm(initial={'action_id': action.id, 'user_id': request.user.id})
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('action_detail', args=[action_id]))
    else:
        form = MessageForm(initial={'action_id': action_id, 'user_id': request.user.id})
    return render(request, 'message/message_form.html', {'form': form})

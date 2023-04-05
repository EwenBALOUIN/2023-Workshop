from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import ActionForm
from ..models import Action
from ..models import Customer
from ..models import Message
from django.contrib.auth.decorators import login_required

@login_required
def action_list(request):
    actions = Action.objects.all().order_by('scheduled_at')
    return render(request, 'action/action_list.html', {'actions': actions})

def action_detail(request, pk):
    action = get_object_or_404(Action, pk=pk)
    messages = Message.objects.filter(action=action).order_by('-created_at')
    return render(request, 'action/action_detail.html', {'action': action, 'messages': messages})

def action_create(request):
    customer = None
    if request.GET.get('customer_id'):
        customer_id = request.GET.get('customer_id', None)
        customer = Customer.objects.get(pk=customer_id)
        form = ActionForm(initial={'customer': customer.pk})
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            form.save()
            if request.GET.get('from'):
                provider = request.GET.get('from', None)
                if provider == 'dashboard':
                    return redirect('dashboard')
                elif provider == 'customer':
                    return redirect('customer_detail', pk=customer.pk)
                elif provider == 'lead':
                    return redirect('lead_detail', pk=customer.pk)
                elif provider == 'prospect':
                    return redirect('prospect_detail', pk=customer.pk)
                else:
                    return redirect('action_list')
    else:
        if customer:
            form = ActionForm(initial={'customer': customer.pk})
        else:
            form = ActionForm()
    return render(request, 'action/action_form.html', {'form': form})

def action_edit(request, pk):
    action = get_object_or_404(Action, pk=pk)
    if request.method == 'POST':
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            action = form.save()
            return redirect('action_list')
    else:
        form = ActionForm(instance=action)
    return render(request, 'action/action_form.html', {'form': form})

def action_delete(request, pk):
    action = get_object_or_404(Action, pk=pk)
    if request.method == 'POST':
        action.delete()
        return redirect('action_list')
    return render(request, 'action/action_confirm_delete.html', {'action': action})
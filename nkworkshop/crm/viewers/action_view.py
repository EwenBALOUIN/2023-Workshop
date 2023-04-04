from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import ActionForm
from ..models import Action
from ..models import Customer
from django.contrib.auth.decorators import login_required

@login_required
def action_list(request):
    actions = Action.objects.all().order_by('scheduled_at')
    return render(request, 'action/action_list.html', {'actions': actions})

# def action_detail(request, pk):
#     action = get_object_or_404(Action, pk=pk)
#     return render(request, 'action/action_detail.html', {'action': action})

def action_create(request):
    if request.GET.get('customer_id'):
        customer_id = request.GET.get('customer_id', None)
        customer = Customer.objects.get(pk=customer_id)
        form = ActionForm(initial={'customer': customer.pk})
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('action_list')
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
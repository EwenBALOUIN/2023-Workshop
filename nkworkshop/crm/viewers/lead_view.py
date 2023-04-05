from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import CustomerForm
from ..models import Customer
from ..models import Action

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

@login_required
def lead_list(request):
    leads = Customer.objects.filter(Q(status='lead') | Q(status='lead mort'))
    return render(request, 'lead/lead_list.html', {'leads': leads})

def lead_detail(request, pk):
    lead = get_object_or_404(Customer, pk=pk)
    actions = Action.objects.filter(customer=lead).order_by('scheduled_at')
    return render(request, 'lead/lead_detail.html', {'lead': lead, 'actions': actions})

def lead_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            lead = form.save()
            return redirect('lead_list')
    else:
        form = CustomerForm()
    return render(request, 'lead/lead_form.html', {'form': form})

def lead_edit(request, pk):
    lead = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=lead)
        if form.is_valid():
            lead = form.save()
            return redirect('lead_list')
    else:
        form = CustomerForm(instance=lead)
    return render(request, 'lead/lead_form.html', {'form': form})

def lead_delete(request, pk):
    lead = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('lead_list')
    return render(request, 'lead/lead_confirm_delete.html', {'lead': lead})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import CustomerForm
from ..models import Customer
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def prospect_list(request):
    prospects = Customer.objects.filter(Q(status='prospect') | Q(status='prospect mort'))
    return render(request, 'prospect/prospect_list.html', {'prospects': prospects})

def prospect_detail(request, pk):
    prospect = get_object_or_404(Customer, pk=pk)
    return render(request, 'prospect/prospect_detail.html', {'prospect': prospect})

def prospect_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            prospect = form.save()
            return redirect('prospect_detail', pk=prospect.pk)
    else:
        form = CustomerForm()
    return render(request, 'prospect/prospect_form.html', {'form': form})

def prospect_edit(request, pk):
    prospect = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=prospect)
        if form.is_valid():
            prospect = form.save()
            return redirect('prospect_detail', pk=prospect.pk)
    else:
        form = CustomerForm(instance=prospect)
    return render(request, 'prospect/prospect_form.html', {'form': form})

def prospect_delete(request, pk):
    prospect = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        prospect.delete()
        return redirect('prospect_list')
    return render(request, 'prospect/prospect_confirm_delete.html', {'prospect': prospect})
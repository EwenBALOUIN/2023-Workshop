from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import CustomerForm
from ..models import Customer
from ..models import Action
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

@login_required
def customer_list(request):
    customers = Customer.objects.filter(Q(status='client') | Q(status='aucun'))
    return render(request, 'customer/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    actions = Action.objects.filter(customer=customer).order_by('scheduled_at')
    return render(request, 'customer/customer_detail.html', {'customer': customer, 'actions': actions})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_form.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer/customer_confirm_delete.html', {'customer': customer})
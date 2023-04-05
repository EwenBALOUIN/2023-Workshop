from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..forms import CompanyForm
from ..models import Company
from django.contrib.auth.decorators import login_required

@login_required
def company_list(request):
    companys = Company.objects.all()
    return render(request, 'company/company_list.html', {'companys': companys})

# def company_detail(request, pk):
#     company = get_object_or_404(Company, pk=pk)
#     return render(request, 'company/company_detail.html', {'company': company})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company/company_form.html', {'form': form})

def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            form.save_m2m()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company/company_form.html', {'form': form})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'company/company_confirm_delete.html', {'company': company})
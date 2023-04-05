from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from crm.models import Customer

@login_required
def dashboard(request):
    nb_contacts = 0
    nb_client = 0
    nb_lead = 0
    nb_prospect = 0
    conversion_rate = '0%'
    nb_contacts = Customer.objects.all().count()
    nb_client = Customer.objects.filter(status="client").count()
    nb_lead = Customer.objects.filter(status="lead").count()
    nb_prospect = Customer.objects.filter(status="prospect").count()
    conversion_rate = str(round(nb_client / nb_contacts * 100, 2)) + '%'
    return render(request, 'dashboard.html', {'nb_contacts': 0, 'nb_client': nb_client, 'nb_lead': nb_lead, 'nb_prospect': nb_prospect, 'conversion_rate': conversion_rate})



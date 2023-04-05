from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from crm.models import Customer
from crm.models import Action
from django.shortcuts import redirect
from django.utils import timezone
from itertools import chain


@login_required
def dashboard(request):
    nb_contacts = 0
    nb_client = 0
    nb_lead = 0
    nb_prospect = 0
    conversion_rate = "0%"
    nb_contacts = Customer.objects.all().count()
    nb_client = Customer.objects.filter(status="client").count()
    nb_lead = Customer.objects.filter(status="lead").count()
    nb_prospect = Customer.objects.filter(status="prospect").count()
    conversion_rate = str(round(nb_client / nb_contacts * 100, 2)) + "%"
    actions_proccessing = Action.objects.filter(done_at=None).order_by("scheduled_at")
    actions_finished= Action.objects.exclude(done_at=None).order_by("scheduled_at")
    
    result_list = list(chain(actions_proccessing, actions_finished))
    return render(
        request,
        "dashboard.html",
        {
            "nb_contacts": 0,
            "nb_client": nb_client,
            "nb_lead": nb_lead,
            "nb_prospect": nb_prospect,
            "conversion_rate": conversion_rate,
            "actions": result_list,
        },
    )


def handle_customer_dead_status(action):
    customer = action.customer
    if customer.status == "prospect":
        customer.status = "prospect mort"
    elif customer.status == "lead":
        customer.status = "lead mort"
    elif customer.status == "client":
        customer.status = "aucun"
    customer.save()


def handle_customer_status(action):
    customer = action.customer
    if action.action_type == "Vente" and (customer.status == "prospect" or customer.status == "prospect dead"):
        customer.status = "client"
    if customer.status == "aucun":
        customer.status = "lead"
    if customer.status == "lead" or customer.status == "lead mort":
        customer.status = "prospect"
    customer.save()


def close_action(request, pk):
    action = Action.objects.get(pk=pk)
    action.done_at = timezone.now()
    handle_customer_dead_status(action)
    action.save()
    return redirect("dashboard")


def validate_action(request, pk):
    action = Action.objects.get(pk=pk)
    action.done_at = timezone.now()
    handle_customer_status(action)
    action.save()
    return redirect("dashboard")


def delete_action(request, pk):
    action = Action.objects.get(pk=pk)
    action.delete()
    return redirect("dashboard")

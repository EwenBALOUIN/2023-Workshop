from django import template
from ..models import Company
from django.utils import timezone

register = template.Library()

@register.filter
def has_company(customer):
    """
    Retourne True si le client a une société.
    """
    company = Company.objects.filter(contacts__pk=customer.pk)
    return company.exists()

@register.filter
def calculate_remaining_time(action):
    date_todo = action.scheduled_at - timezone.now()
    if date_todo.days > 0:
        return str(date_todo.days) + ' jours'
    elif date_todo.seconds > 3600:
        return str(date_todo.seconds // 3600) + ' heures'
    elif date_todo.seconds > 60:
        return str(date_todo.seconds // 60) + ' minutes'
    else:
        return str(date_todo.seconds) + ' secondes'
    
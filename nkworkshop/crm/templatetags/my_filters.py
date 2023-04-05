from django import template
from ..models import Company

register = template.Library()

@register.filter
def has_company(customer):
    """
    Retourne True si le client a une société.
    """
    company = Company.objects.filter(contacts__pk=customer.pk)
    return company.exists()
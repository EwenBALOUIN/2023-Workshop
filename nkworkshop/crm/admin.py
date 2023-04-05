from django.contrib import admin

# Register your models here.

from .models.customer import Customer
from .models.action import Action
from .models.company import Company
from .models.message import Message


admin.site.register(Customer)
admin.site.register(Action)
admin.site.register(Company)
admin.site.register(Message)
from django.contrib import admin

# Register your models here.

from .models.customer import Customer
from .models.action import Action
from .models.company import Company


admin.site.register(Customer)
admin.site.register(Action)
admin.site.register(Company)
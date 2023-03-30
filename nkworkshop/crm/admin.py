from django.contrib import admin

# Register your models here.

from .models.customer import Customer

admin.site.register(Customer)
from django.urls import path
from crm.viewers import customer_view


urlpatterns = [
    # Customer
    path('customer/', customer_view.customer_list, name='customer_list'),
    path('customer/<int:pk>/', customer_view.customer_detail, name='customer_detail'),
    path('customer/create/', customer_view.customer_create, name='customer_create'),
    path('customer/edit/<int:pk>', customer_view.customer_edit, name='customer_edit'),
    path('customer/delete/<int:pk>', customer_view.customer_delete, name='customer_delete')


]
from django.urls import path
from crm.viewers import company_view

urlpatterns = [
    # company
    path('company/', company_view.company_list, name='company_list'),
    # path('company/<int:pk>/', company_view.company_detail, name='company_detail'),
    path('company/create/', company_view.company_create, name='company_create'),
    path('company/edit/<int:pk>', company_view.company_edit, name='company_edit'),
    path('company/delete/<int:pk>', company_view.company_delete, name='company_delete'),
]
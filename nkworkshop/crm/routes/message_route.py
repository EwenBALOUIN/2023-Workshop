from django.urls import path
from crm.viewers import message_view

urlpatterns = [
    # Lead
    # path('lead/', lead_view.lead_list, name='lead_list'),
    # path('lead/<int:pk>/', lead_view.lead_detail, name='lead_detail'),
    path('message/create/', message_view.message_create, name='message_create'),
    # path('lead/edit/<int:pk>', lead_view.lead_edit, name='lead_edit'),
    # path('lead/delete/<int:pk>', lead_view.lead_delete, name='lead_delete'),
]
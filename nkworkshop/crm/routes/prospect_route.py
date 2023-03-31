from django.urls import path
from crm.viewers import prospect_view

urlpatterns = [
    # Prospect
    path('prospect/', prospect_view.prospect_list, name='prospect_list'),
    # path('prospect/<int:pk>/', prospect_view.prospect_detail, name='prospect_detail'),
    path('prospect/create/', prospect_view.prospect_create, name='prospect_create'),
    path('prospect/edit/<int:pk>', prospect_view.prospect_edit, name='prospect_edit'),
    path('prospect/delete/<int:pk>', prospect_view.prospect_delete, name='prospect_delete'),
]

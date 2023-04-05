from django.urls import path
from crm.viewers import dashboard_view

urlpatterns = [
    path('', dashboard_view.dashboard, name='dashboard'),
    path('close-action/<int:pk>/', dashboard_view.close_action, name='close_action'),
    path('valid-action/<int:pk>/', dashboard_view.validate_action, name='valid_action'),
    path('delete-action/<int:pk>/', dashboard_view.delete_action, name='delete_action'),
]
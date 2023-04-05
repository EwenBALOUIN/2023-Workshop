from django.urls import path
from crm.viewers import action_view

urlpatterns = [
    # Action
    path('action/', action_view.action_list, name='action_list'),
    path('action/<int:pk>/', action_view.action_detail, name='action_detail'),
    path('action/create/', action_view.action_create, name='action_create'),
    path('action/edit/<int:pk>', action_view.action_edit, name='action_edit'),
    path('action/delete/<int:pk>', action_view.action_delete, name='action_delete'),
]
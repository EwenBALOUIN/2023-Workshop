from django.urls import path, include
from .viewers.home import HomeView
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.urls import re_path
from .routes import customer_route as customer_route
from .routes import lead_route as lead_route
from .routes import prospect_route as prospect_route
from .routes import action_route as action_route



urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download'),
    re_path('.*login/', views.logincrm, name='login'),
    re_path('.*logout/', views.logoutcrm, name='logout'),

    path('', include(customer_route)),
    path('', include(lead_route)),
    path('', include(prospect_route)),
    path('', include(action_route)),
    # # Customer
    # path('customer/', customer_view.customer_list, name='customer_list'),
    # path('customer/<int:pk>/', customer_view.customer_detail, name='customer_detail'),
    # path('customer/create/', customer_view.customer_create, name='customer_create'),
    # path('customer/edit/<int:pk>', customer_view.customer_edit, name='customer_edit'),
    # path('customer/delete/<int:pk>', customer_view.customer_delete, name='customer_delete'),
    # # Lead
    # path('lead/', lead_view.lead_list, name='lead_list'),
    # path('lead/<int:pk>/', lead_view.lead_detail, name='lead_detail'),
    # path('lead/create/', lead_view.lead_create, name='lead_create'),
    # path('lead/edit/<int:pk>', lead_view.lead_edit, name='lead_edit'),
    # path('lead/delete/<int:pk>', lead_view.lead_delete, name='lead_delete'),
    # # Prospect
    # path('prospect/', prospect_view.prospect_list, name='prospect_list'),
    # path('prospect/<int:pk>/', prospect_view.prospect_detail, name='prospect_detail'),
    # path('prospect/create/', prospect_view.prospect_create, name='prospect_create'),
    # path('prospect/edit/<int:pk>', prospect_view.prospect_edit, name='prospect_edit'),
    # path('prospect/delete/<int:pk>', prospect_view.prospect_delete, name='prospect_delete'),
    # # User
    # # path('user/', customer_view.user_list, name='user_list'),
    # # path('user/<int:pk>/', customer_view.user_detail, name='user_detail'),
    # # path('user/create/', customer_view.user_create, name='user_create'),
    # # path('user/edit/<int:pk>', customer_view.user_edit, name='user_edit'),
    # # path('user/delete/<int:pk>', customer_view.user_delete, name='user_delete'),
    # # Action
    # path('action/', action_view.action_list, name='action_list'),
    # path('action/<int:pk>/', action_view.action_detail, name='action_detail'),
    # path('action/create/', action_view.action_create, name='action_create'),
    # path('action/edit/<int:pk>', action_view.action_edit, name='action_edit'),
    # path('action/delete/<int:pk>', action_view.action_delete, name='action_delete'),


]
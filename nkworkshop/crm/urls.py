from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.urls import re_path
from .routes import customer_route as customer_route
from .routes import lead_route as lead_route
from .routes import prospect_route as prospect_route
from .routes import action_route as action_route
from .routes import company_route as company_route
from .routes import user_route as user_route
from .viewers import dashboard_view


urlpatterns = [
    path('', dashboard_view.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download'),
    re_path('.*login/', views.logincrm, name='login'),
    re_path('.*logout/', views.logoutcrm, name='logout'),

    path('', include(customer_route)),
    path('', include(lead_route)),
    path('', include(prospect_route)),
    path('', include(action_route)),
    path('', include(company_route)),
    path('', include(user_route))
]
from django.urls import path
from .viewers.home import HomeView
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.urls import re_path

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download'),
    re_path('.*login/', views.logincrm, name='login'),
]
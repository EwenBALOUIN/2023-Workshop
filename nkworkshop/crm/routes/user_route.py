from django.urls import path
from crm.viewers import user_view


urlpatterns = [
    # user
    path('user/', user_view.user_list, name='user_list'),
    # path('user/<int:pk>/', user_view.user_detail, name='user_detail'),
    path('user/create/', user_view.user_create, name='user_create'),
    path('user/edit/<int:pk>', user_view.user_edit, name='user_edit'),
    path('user/delete/<int:pk>', user_view.user_delete, name='user_delete')
]
from django.conf.urls import url
from django.urls import path
from .views import success, create_contactlist, edit_contactlist, contactlist_list, delete_contactlist

urlpatterns = [
    path('success/', success, name='success'),
    path('create_contactlist/', create_contactlist, name='create_contactlist'),
    path('edit_contactlist/<int:contactlist_id>/', edit_contactlist, name='edit_contactlist'),
    path('contactlist_list/', contactlist_list, name='contactlist_list'),
    path('delete_contactlist/<int:contactlist_id>/', delete_contactlist, name='delete_contactlist'),
]

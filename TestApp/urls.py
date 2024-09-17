from django.contrib import admin
from django.urls import path
from django.urls import include
from TestApp.views import *
urlpatterns = [
    path('', index, name='index'),
    path('contact-list/', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
    path('<int:id>/formupdate/', formupdate, name='formupdate'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>',delete,name='delete'),
    path('search/', search_contacts, name='search_contacts'),
]
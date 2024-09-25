from django.urls import path
from .views import home, create_contact, delete_contact

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_contact, name='create_contact'),
    path('delete/', delete_contact, name='delete_contact'),
]

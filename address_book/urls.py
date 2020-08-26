from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('downloads', views.downloads, name='downloads'),
    path('add_address', views.add_address, name='add_address'),
    path('addresses', views.addresses, name='addresses'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('delete/<list_id>', views.delete, name='delete'),
]
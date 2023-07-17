from django.urls import path

from . import views


urlpatterns = [
    path('get_manufacturers_ids/<int:contract_id>', views.get_manufacturers_ids)
]

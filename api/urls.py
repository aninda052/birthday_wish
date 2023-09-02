# external imports
from django.urls import path

# internal imports
from .views.customer import CustomerViewset

urlpatterns = [
    path('add-customer/', CustomerViewset.as_view(), name='add_customer'),
]
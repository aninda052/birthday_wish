# external imports
from rest_framework import generics
from rest_framework.permissions import AllowAny

# internal imports
from ..serializers.customer import CustomerSerializer
from customer.models import Customer

class CustomerViewset(generics.CreateAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [AllowAny]
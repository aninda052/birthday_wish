# external imports
from rest_framework import serializers

# internal imports
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'date_of_birth'
        ]
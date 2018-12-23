from rest_framework import serializers
from app_contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'full_name',
            'home_no',
            'mobile_no',
            'address',
        )

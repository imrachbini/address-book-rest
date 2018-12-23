from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from app_contacts.models import Contact
from app_contacts.serializers import ContactSerializer


class ContactList(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, pk, format=None):
        try:
            contact_detail = Contact.objects.get(id=pk)
            serializer = self.get_serializer(contact_detail)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            body = {
                'message': 'Contact not found',
            }
            return Response(body, 404)

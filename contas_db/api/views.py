from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from contas_db.models import Contact
from .authentication import BearerAuthentication
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
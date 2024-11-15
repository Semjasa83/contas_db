from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from contas_db.models import Contact
from contas_db.api.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet): # viewset ModelViewSet
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
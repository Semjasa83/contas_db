from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from contas_db.models import Contact, Note
from .authentication import BearerAuthentication
from .serializers import ContactSerializer, NoteSerializer


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
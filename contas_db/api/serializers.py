from rest_framework import serializers
from contas_db.models import Contact, Note


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id",
            "firstname",
            "lastname",
            "email",
            "phone",
            "note",
            "color",
            "company",
            "created_at",
            "updated_at",
        )


class NoteSerializer(serializers.ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)
    class Meta:
        model = Note
        fields = (
            "id",
            "contact",
            "company",
            "headline",
            "note",
            "start_date",
            "end_date",
            "color",
            "priority",
            "created_at",
            "updated_at",
        )
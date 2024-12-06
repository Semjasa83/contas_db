from rest_framework import serializers
from contas_db.models import Contact


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
            "created_at",
            "updated_at",
        )

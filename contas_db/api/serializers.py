from rest_framework import serializers
from contas_db.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id',
                  'name',
                  'email',
                  'phone',
                  'street',
                  'city',
                  'zip',
                  'country',
                  'note',
                  'created_at',
                  'updated_at'
                  )

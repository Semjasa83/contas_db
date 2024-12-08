from rest_framework import serializers
from user_auth_app.models import UserProfile

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "created_at",
            "updated_at"
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
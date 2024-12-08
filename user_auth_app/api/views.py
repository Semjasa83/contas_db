from user_auth_app.api.utils import emailAuthentification
from user_auth_app.models import UserProfile
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegistrationView(APIView):

    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serialiser = RegistrationSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            user = User.objects.get(email=serialiser.data['email'])
            token, created = Token.objects.get_or_create(user=user)
            emailAuthentification(user, token)
            
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        if serialiser.errors:
            return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


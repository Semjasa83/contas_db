from user_auth_app.api.utils import email_authentification
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny



class RegistrationView(APIView):

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_user_model(data=request.data['email'])
            token, created = Token.objects.get_or_create(user=user)
            email_authentification(user, token)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


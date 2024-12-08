from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

def email_authentification(user, token):
    context = {
        'user': user.username,
        'token': token.key
    }
    rendered = render_to_string('activation.html', context)
    subject = 'Activate your Contas Account'
    html_message = rendered
    email_from = 'marceldezanna+contas@yahoo.de' #MEINE MAIL
    recipient_list = [user.email,]
    send_mail(subject, html_message, email_from, recipient_list, fail_silently=True)


@api_view(['GET',])
def activate_user(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    token = Token.objects.get(user=user)
    
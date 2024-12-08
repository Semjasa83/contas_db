from django.template.loader import render_to_string
from django.core.mail import send_mail

def emailAuthentification(user, token):
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
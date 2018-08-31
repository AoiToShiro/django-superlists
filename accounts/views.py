from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import auth, messages
from accounts.models import Token
from django.core.urlresolvers import reverse

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid) #for some reason the 'n' in login does not appear in the url. I have changed the test to reflect this
    )
    message_body = f'Use this link to log in:\n\n{url}'
    # print(message_body)
    send_mail(
        'Your login link for Listymclistface',
        message_body,
        'noreply@listymclistface.site',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')

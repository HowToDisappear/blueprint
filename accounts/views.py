from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User

from accounts.models import Account
from .forms import LoginForm, RegisterForm, AccountFormUser, AccountFormAccount

# token generator instance
tokenGenerator = PasswordResetTokenGenerator()

# Create your views here.
def login(request):
    auth_msg = ''
    if request.method == 'POST':
        uform = LoginForm(request.POST)
        if uform.is_valid():
            user = authenticate(username=uform.cleaned_data['username'], password=uform.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/art/')
            else:
                auth_msg = 'No user match for username and password provided. Please try again.'
    elif request.method == 'GET':
        uform = LoginForm()
    return render(request, 'accounts/logreg.html', {
        'uform': uform,
        'type': 'login',
        'auth_msg': auth_msg,
        })

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/art/')

def register(request):
    user_created = False
    if request.method == 'POST':
        uform = RegisterForm(request.POST)
        if uform.is_valid():
            user = uform.save(commit=False)
            user.set_password(uform.cleaned_data['password'])
            user.is_active = False
            user.save()
            # create account for the user
            account = Account(user=user)
            account.save()
            email_conf(user)
            user_created = True
    elif request.method == 'GET':
        uform = RegisterForm()
    return render(request, 'accounts/logreg.html', {
        'uform': uform,
        'type': 'register',
        'user_created': user_created,
        })

def email_conf(user):
    token = tokenGenerator.make_token(user)
    username = user.username
    uid = urlsafe_base64_encode(force_bytes(user.id))
    msg = EmailMessage(
        subject='email confirmation',
        body=f'<p>Hello, to activate your account <strong>{username}</strong> please follow the link: <a href="http://127.0.0.1:8000/accounts/activate/{uid}/{token}">Activate<a></p>',
        to=[user.email]
    )
    msg.content_subtype = 'html'
    msg.send()

def activate(request, uid, token):
    try:
        uid_clean = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid_clean)
    except:
        user = None
    check_result = tokenGenerator.check_token(user, token)
    if user is not None and check_result:
        user.is_active = True
        user.save()
        # ! replace automatical logging in with 'success' notification !
        auth_login(request, user)
        return HttpResponseRedirect('/art/')
    else:
        return HttpResponse('Something went wrong.')


def account(request, account):
    user = User.objects.get(id=account.split('-')[1])
    user_account = user.account

    if request.method == 'POST' and request.user.is_authenticated:
        if request.POST['av_action']:
            if request.POST['av_action'] == 'delete':
                user_account.image.delete()
                user_account.crop_params = ''
                user_account.save()
                return HttpResponseRedirect(request.path_info)

            elif request.POST['av_action'] == 'replace':
                user_account.image.delete()
                user_account.crop_params = ''
                user_account.save()
        
        img = user_account.image
        uform = AccountFormUser(request.POST, instance=user)
        aform = AccountFormAccount(request.POST, request.FILES, instance=user_account)
        if uform.is_bound and uform.is_valid():
            uform.save()
        if aform.is_bound and aform.is_valid() and request.POST['av_action']:
            if img:
                user_account.crop = True
                user_account.save()
            aform.save()
        return HttpResponseRedirect(request.path_info)

    uform = AccountFormUser(label_suffix="")
    aform = AccountFormAccount(label_suffix="")
    context = {
        'uform':uform,
        'aform':aform,
    }
    return render(request, 'accounts/account.html', context)

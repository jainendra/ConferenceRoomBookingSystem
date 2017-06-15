from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from forms import SignupForm


def signup(request):
    """
    This function
        - returns view for signup page
        - handles http request for signup
        - creates new user
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    user = request.user
    if user.is_authenticated():
        return redirect('booking:home')
    if request.method == 'POST':
        signup_form = SignupForm(data=request.POST, prefix='signup', auto_id='id_signup_%s')
        message = ''
        if signup_form.is_valid():
            if signup_form.save():
                message = 'You account has been created, you may login with your entered credentials'
            else:
                message = 'You account has not been created, some error occurred'

        context = {
            'signup_form': signup_form,
            'message': message
        }
        return render(request, 'signup.html', context)
    else:
        signup_form = SignupForm(prefix='signup', auto_id='id_signup_%s')
        context = {
            'signup_form': signup_form
        }
        return render(request, 'signup.html', context)


def login(request):
    """
    This function
        - returns view for login page
        - handles http request for login
        - logs in user with correct credentials
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    user = request.user
    if user.is_authenticated():
        return redirect('booking:home')
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST, prefix='login', auto_id='id_login_%s')

        if login_form.is_valid():
            # Django treats unique identifiers as username,  so here email is referred as username
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('booking:home')

        context = {
            'login_form': login_form
        }

        return render(request, 'login.html', context)
    else:
        login_form = AuthenticationForm(prefix='login', auto_id='id_login_%s')
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context)


@login_required
def logout(request):
    """
    This function
        - logs out a logged in user
        - redirects to login/signup page
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    auth.logout(request)
    return redirect('booking:login')


@login_required
def home(request):
    """
    This function
        - generates landing page for CRBS logged in user
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    context = {}
    return render(request, 'home.html', context)

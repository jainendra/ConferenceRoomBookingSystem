from django.shortcuts import render, redirect, Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from forms import SignupForm


def index(request):
    """
    This function
        - generates view for landing page of CRBS for a non-authenticated/not-logged in user
        - contain login and signup page
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    user = request.user
    if user.is_authenticated():
        return redirect('booking:home')
    else:
        login_form = AuthenticationForm()
        signup_form = SignupForm()
        context = {
            'login_form': login_form,
            'signup_form': signup_form
        }
        return render(request, 'index.html', context)


def signup(request):
    """
    This function
        - handles post request for signup
        - creates new user
        - logs in the new user
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    if request.method == 'POST':
        signup_form = SignupForm(data=request.POST)
        if signup_form.is_valid():
            if signup_form.save():
                # TODO: Add login code and confirmation message for signed In user
                return redirect('booking:index')
            else:
                return redirect('booking:index')

        context = {
            'signup_form': signup_form
        }
        return render(request, 'index.html', context)
    else:
        raise Http404


def login(request):
    """
    This function
        - handles post request for login
        - logs in user with correct credentials
    :param request: HttpRequest
    :return: HttpResponseObject
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('booking:home')

        context = {
            'login_form': login_form
        }

        return render(request, 'index.html', context)
    else:
        raise Http404


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
    return redirect('booking:index')


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

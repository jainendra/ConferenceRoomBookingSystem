"""
This file contains all the functions available via API URL
api function acts as an interface between all the request and functions response
All the functions defined below returns a JSON object
"""

from django.http import JsonResponse
from django.shortcuts import Http404
import json


def api(request):
    if not request.POST:
        raise Http404
    else:
        json_data = json.load(request.body)
        # if request.POST['data_code'] == 1:
        #     return signup(request)
        # elif request.POST['data_code'] == 2:
        #     return login(request)
        # elif request.POST['data_code'] == 3:
        #     return logout(request)
        # else:
        #     pass
        # TODO: Code all the cases according to data_code value
        return JsonResponse(json_data)


def signup(request):
    """
    This function creates a new user
    :param request:
    :return: JSON Object
    """
    json = {
        'status_code': 1,
        'message': 'Test Successful'
    }
    return JsonResponse(json)


def login(request):
    """
    This function authenticates the user upon correct credentials and creates a session
    :param request:
    :return: JSON Object
    """
    json = {
        'status_code': 1,
        'message': 'Test Successful'
    }
    return JsonResponse(json)


def logout(request):
    """
    This function destroys the session of the logged in user
    :param request:
    :return: JSON Object
    """
    json = {
        'status_code': 1,
        'message': 'Test Successful'
    }
    return JsonResponse(json)

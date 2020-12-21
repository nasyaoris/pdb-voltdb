from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import json


def loginPage(request):
    if (request.session['usernamme'] != ''):
        return HttpResponseRedirect('/registration/success')
    return render(request, "login.html")


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        request.session['usernamme'] = username
        # Redirect to a success page.
        return HttpResponseRedirect('/registration/success')
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/registration/login')


def successPage(request):
    return render(request, "success.html")

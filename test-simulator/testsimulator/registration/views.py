from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from voltdbclient import *


def loginPage(request):
    # if (request.session['username'] != ''):
    #     return HttpResponseRedirect('/registration/success')
    return render(request, "login.html")


def login(request):
    if (request.method === "POST")
    client = FastSerializer('localhost', 33281)

    username = request.POST.get('username')
    password = request.POST.get('password')

    proc = VoltProcedure(client, "Login", [FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_STRING])
    user = proc.call([username, password])

    table = user.tables[0]

    if (table === None):
        return HttpResponseRedirect('/registration/login')
    else:
        request.session['username'] = table.tuples[0][0]
        return HttpResponseRedirect('/soal/1')

    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     auth_login(request, user)
    #     request.session['username'] = username
    #     # Redirect to a success page.
    #     return HttpResponseRedirect('/registration/success')
    # else:
    #     # Return an 'invalid login' error message.
    #     return HttpResponseRedirect('/registration/login')


def successPage(request):
    return render(request, "success.html")

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from voltdbclient import *


def loginPage(request):
    return render(request, "login.html")


def login(request):

    client = FastSerializer("localhost", 49154)

    if request.method == "POST":
        client = FastSerializer("localhost", 49154)

    username = request.POST.get('username')
    password = request.POST.get('password')

    proc = VoltProcedure(client, "Login", [FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_STRING])
    user = proc.call([username, password])

    table = user.tables[0]

    try:
        if (table.tuples[0][0] == username):
            request.session['username'] = table.tuples[0][0]
            return HttpResponseRedirect('/soal/1')
    except:
        return HttpResponseRedirect('/registration/loginPage')

def successPage(request):
    return render(request, "success.html")

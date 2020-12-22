from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json


def soalPage(request, id):
    return HttpResponseRedirect('/registration/success') #Change this to render soal page
from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import SoalModel
from jawaban.models import JawabanModel
from pilihanJawaban.models import PilihanJawabanModel
import json


def soalPage(request,soal_id):
    soal = get_object_or_404(SoalModel, id=soal_id)
    pilihan_jawaban = []
    semua_jawaban = PilihanJawabanModel.objects.all()
    semua_jawaban = list(semua_jawaban)
    for jawaban in semua_jawaban:
        if jawaban.soal.id == soal.id:
            pilihan_jawaban.append(jawaban)
    context = {
        'pilihan_jawaban' : pilihan_jawaban,
        'soal' : soal,
        'soal_id' : soal_id
        }
    return render(request, "soal.html", context)

def submit_jawaban(request):
    jawaban = request.POST.get('jawaban')
    soal = request.POST.get('soal')
    user = request.user
    print(soal)
    print(user)
    print(jawaban)
    #submit = JawabanModel(id_user = user, id_jawaban = jawaban)
    #string = "user id = " + user + "id jawaban = " + jawaban
    return HttpResponseRedirect('/soal/submit_jawaban/')



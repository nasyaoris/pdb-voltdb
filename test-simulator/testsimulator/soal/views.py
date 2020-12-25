from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import SoalModel
from jawaban.models import JawabanModel
from registration.models import UserProfile
from pilihanJawaban.models import PilihanJawabanModel
from django.contrib.auth.models import User
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
    user = UserProfile.objects.get(nama=request.user.username)
    answer = JawabanModel(id_soal=SoalModel(soal), id_pilihan=PilihanJawabanModel(jawaban), id_user=user)
    answer.save()
    totalSoal = len(SoalModel.objects.all())
    nextSoal = int(soal) + 1
    if nextSoal <= totalSoal:
        return HttpResponseRedirect('/soal/%d/' % nextSoal)
    else:
        return HttpResponseRedirect('/soal/hasil')

def hasil(request):
    user = UserProfile.objects.get(nama=request.user.username)
    jawaban = JawabanModel.objects.filter(id_user=user)
    totalSoal = len(SoalModel.objects.all())
    print(totalSoal)
    score = 0
    print(len(jawaban))
    for ans in jawaban:
        print("in for loop")
        if ans.id_pilihan.id == ans.id_soal.kunci:
            print("in if")
            score += 1

    print(score)
    score = (score/totalSoal) * 100 

    context = {
        'score' : score
    }

    return render(request, "hasil.html", context)


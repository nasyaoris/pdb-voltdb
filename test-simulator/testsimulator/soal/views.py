from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import SoalModel
from jawaban.models import JawabanModel
from registration.models import UserProfile
from pilihanJawaban.models import PilihanJawabanModel
import random
from voltdbclient import *


def soalPage(request,soal_id):
    soal = get_object_or_404(SoalModel, id=soal_id)
    pilihan_jawaban = []
    semua_jawaban = PilihanJawabanModel.objects.all()
    semua_jawaban = list(semua_jawaban)
    for jawaban in semua_jawaban:
        if jawaban.soal.id == soal.id:
            pilihan_jawaban.append(jawaban)

    if len(pilihan_jawaban) > 0:
        random.shuffle(pilihan_jawaban)

    context = {
        'pilihan_jawaban' : pilihan_jawaban,
        'soal' : soal,
        'soal_id' : soal_id
        }
    return render(request, "soal.html", context)

def submit_jawaban(request):

    client = FastSerializer("localhost", 49154)

    jawaban = request.POST.get('jawaban')
    # print(jawaban)
    soal = request.POST.get('soal')
    # print(soal)
    # user = UserProfile.objects.get(nama=request.user.username)
    username = request.user.username
    # print(username)

    procSubmitJawaban = VoltProcedure( client, "SubmitJawaban", [FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_STRING] )

    procSubmitJawaban.call(username, soal, jawaban)

    procGetNextSoal = VoltProcedure( client, "SelectSoalByUrutan", [FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_INTEGER] )

    nextSoal = procGetNextSoal.call(username, ) #Need nomor urut selanjutnya

    if(len(nextSoal.tables) > 0):
        return HttpResponsedRedirect('/soal/%d/' % nextSoal)
    else:
        return HttpResponsedRedirect('/soal/hasil')

    # answer = JawabanModel(id_soal=SoalModel(soal), id_pilihan=PilihanJawabanModel(jawaban), id_user=user)
    # answer.save()
    # allSoal = SoalModel.objects.all()
    # totalSoal = len(allSoal)
    # allJawaban = JawabanModel.objects.filter(id_user=user)
    # totalJawaban = len(allJawaban)
    # answeredIdSoal = []
    # for i in allJawaban:
    #     answeredIdSoal.append(i.id_soal.id)
    # if totalJawaban < totalSoal:
    #     nextSoal = random.choice([i for i in range(1, totalSoal+1) if i not in answeredIdSoal])
    #     return HttpResponseRedirect('/soal/%d/' % nextSoal)
    # else:
    #     return HttpResponseRedirect('/soal/hasil')

def hasil(request):

    client = FastSerializer("localhost", 49154)

    username = request.user.username

    procGetScore = VoltProcedure( client, "GetFinalScore", [FastSerializer.VOLTTYPE_STRING])

    score = procGetScore.call(username)

    # user = UserProfile.objects.get(nama=request.user.username)
    # jawaban = JawabanModel.objects.filter(id_user=user)
    # totalSoal = len(SoalModel.objects.all())
    # score = 0
    # for ans in jawaban:
    #     if ans.id_pilihan.id == ans.id_soal.kunci:
    #         score += 1

    # score = (score/totalSoal) * 100 

    context = {
        'score' : score
    }

    return render(request, "hasil.html", context)


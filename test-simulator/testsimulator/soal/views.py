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


def soalPage(request, urutan):
    client = FastSerializer("localhost", 49154)

    username = request.session['username']

    # username = "user1" ## GANTI USERNAME NYA JADI DARI SESSION

    procGetSoal = VoltProcedure(client, "SelectSoalByUrutan", [FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_INTEGER])
    soal = procGetSoal.call([username, int(urutan)])

    tableSoal = soal.tables[0]

    actualSoal = tableSoal.tuples[0][0]

    procGetPilihan = VoltProcedure(client, "SelectPilihanBySoal", [FastSerializer.VOLTTYPE_STRING])
    pilihan_jawaban = procGetPilihan.call([actualSoal])
    tablePilihan = pilihan_jawaban.tables[0]

    idPilihan = list(zip(*tablePilihan.tuples))[0]
    namaPilihan = list(zip(*tablePilihan.tuples))[2]

    context = {
        'pilihan_jawaban_id_1' : idPilihan[0],
        'pilihan_jawaban_nama_1': namaPilihan[0],
        'pilihan_jawaban_id_2' : idPilihan[1],
        'pilihan_jawaban_nama_2': namaPilihan[1],
        'pilihan_jawaban_id_3' : idPilihan[2],
        'pilihan_jawaban_nama_3': namaPilihan[2],
        'pilihan_jawaban_id_4' : idPilihan[3],
        'pilihan_jawaban_nama_4': namaPilihan[3],
        'soal' : tableSoal.tuples[0][1],
        'soal_id' : tableSoal.tuples[0][0],
        'urutan' : urutan
    }
    return render(request, "soal.html", context)

def submit_jawaban(request):

    req = request.META.get('HTTP_REFERER')
    urutan = int(req[-3:-1])
    print(urutan)

    client = FastSerializer("localhost", 49154) ## Sesuaikan port dengan container di docker

    jawaban = request.POST.get('jawaban')

    soal = request.POST.get('soal')

    username = request.session['username']

    # username = "user1" ## GANTI USERNAME NYA JADI DARI SESSION

    procSubmitJawaban = VoltProcedure( client, "SubmitJawaban", [FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_STRING, FastSerializer.VOLTTYPE_STRING] )

    procSubmitJawaban.call([username, soal, jawaban])
    if(urutan < 50):
        urutan +=1
        return HttpResponseRedirect('/soal/%d/' % urutan)
    else:
        return HttpResponseRedirect('/soal/hasil')

def hasil(request):

    client = FastSerializer("localhost", 49154)

    username = request.session['username']

    procFinishTest = VoltProcedure( client, "FinishTest", [FastSerializer.VOLTTYPE_STRING])

    finish = procFinishTest.call([username])

    procGetScore = VoltProcedure( client, "GetFinalScore", [FastSerializer.VOLTTYPE_STRING])

    score = procGetScore.call([username])

    context = {
        'score' : score.tables[0].tuples[0][0]
    }

    return render(request, "hasil.html", context)


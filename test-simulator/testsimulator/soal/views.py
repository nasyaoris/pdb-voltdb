from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import SoalModel
from jawaban.models import JawabanModel
from registration.models import UserProfile
from pilihanJawaban.models import PilihanJawabanModel
from random import choice


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
    allSoal = SoalModel.objects.all()
    totalSoal = len(allSoal)
    allJawaban = JawabanModel.objects.filter(id_user=user)
    totalJawaban = len(allJawaban)
    answeredIdSoal = []
    for i in allJawaban:
        answeredIdSoal.append(i.id_soal.id)
    if totalJawaban < totalSoal:
        nextSoal = choice([i for i in range(1, totalSoal+1) if i not in answeredIdSoal])
        return HttpResponseRedirect('/soal/%d/' % nextSoal)
    else:
        return HttpResponseRedirect('/soal/hasil')

def hasil(request):
    user = UserProfile.objects.get(nama=request.user.username)
    jawaban = JawabanModel.objects.filter(id_user=user)
    totalSoal = len(SoalModel.objects.all())
    score = 0
    for ans in jawaban:
        if ans.id_pilihan.id == ans.id_soal.kunci:
            score += 1

    score = (score/totalSoal) * 100 

    context = {
        'score' : score
    }

    return render(request, "hasil.html", context)


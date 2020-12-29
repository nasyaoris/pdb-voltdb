from django.db import models

# Create your models here.

from django.db import models
from registration.models import UserProfile
from pilihanJawaban.models import PilihanJawabanModel
from soal.models import SoalModel
# Create your models here.

class JawabanModel(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    id_soal = models.ForeignKey(SoalModel, on_delete = models.CASCADE)
    id_pilihan = models.ForeignKey(PilihanJawabanModel, on_delete = models.CASCADE)

    def __int__(self):
        return self.id
from django.db import models
from soal.models import SoalModel

# Create your models here.

class PilihanJawabanModel(models.Model):
    id = models.IntegerField(primary_key=True)
    pilihan = models.CharField(max_length=200)
    soal = models.ForeignKey(SoalModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.pilihan

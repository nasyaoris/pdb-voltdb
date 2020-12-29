from django.db import models

# Create your models here.

class SoalModel(models.Model):
    id = models.IntegerField(primary_key=True)
    soal = models.CharField(max_length=200)
    kunci = models.IntegerField()

    def __str__(self):
        return self.soal

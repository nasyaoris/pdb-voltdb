from django.db import models

# Create your models here.

class Jadwal(models.Model):
    id_jadwal = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=20)

class Course(models.Model):
    id_course = models.AutoField(primary_key=True, unique=True)
    nama = models.TextField(max_length=30)

class SelectedCourse(models.Model):
    id_selected_course = models.AutoField(primary_key=True, unique=True)
    id_course = models.OneToOneField(Course, on_delete=models.CASCADE)
    timestamp = models.TimeField(auto_now_add=True)
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
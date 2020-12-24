# Generated by Django 3.1.4 on 2020-12-22 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        ('soal', '0001_initial'),
        ('pilihanJawaban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JawabanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pilihan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilihanJawaban.pilihanjawabanmodel')),
                ('id_soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soal.soalmodel')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.userprofile')),
            ],
        ),
    ]
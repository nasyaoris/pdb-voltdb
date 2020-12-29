# Generated by Django 3.1.4 on 2020-12-22 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('soal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PilihanJawabanModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pilihan', models.CharField(max_length=200)),
                ('soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soal.soalmodel')),
            ],
        ),
    ]

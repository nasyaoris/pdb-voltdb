# Generated by Django 3.1.4 on 2020-12-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoalModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('soal', models.CharField(max_length=200)),
                ('kunci', models.IntegerField()),
            ],
        ),
    ]

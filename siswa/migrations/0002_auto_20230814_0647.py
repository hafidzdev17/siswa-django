# Generated by Django 3.2 on 2023-08-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anak',
            name='berat_badan',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='anak',
            name='tinggi_badan',
            field=models.CharField(max_length=10),
        ),
    ]

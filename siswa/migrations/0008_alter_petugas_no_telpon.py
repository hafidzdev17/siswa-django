# Generated by Django 4.2.3 on 2023-07-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0007_alter_petugas_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petugas',
            name='no_telpon',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]

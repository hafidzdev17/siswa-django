# Generated by Django 3.2 on 2023-08-26 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biaya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biaya', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Biaya',
            },
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kelas', models.CharField(max_length=10)),
                ('status_kelas', models.CharField(choices=[('Aktif', 'Aktif'), ('Nonaktif', 'Nonaktif')], default='Aktif', max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Kelas',
            },
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nisn', models.CharField(max_length=10, unique=True)),
                ('nama', models.CharField(max_length=200)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], default='L', max_length=1)),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('ttl', models.DateField()),
                ('tahun_akademik', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('kelas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siswa.kelas')),
            ],
            options={
                'verbose_name_plural': 'Siswa',
            },
        ),
        migrations.CreateModel(
            name='Petugas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_petugas', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Aktif', 'Aktif'), ('Nonaktif', 'Nonaktif')], default='Aktif', max_length=8)),
                ('no_telpon', models.CharField(blank=True, max_length=200, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Petugas',
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pembayaran', models.CharField(max_length=100)),
                ('tahun', models.CharField(max_length=100)),
                ('kategori', models.CharField(blank=True, choices=[('KMS', 'KMS'), ('LKS', 'LKS'), ('Komputer', 'Komputer')], max_length=150)),
                ('tanggal', models.DateField()),
                ('keterangan', models.CharField(blank=True, choices=[('Lunas', 'Lunas'), ('Belum Lunas', 'Belum Lunas')], max_length=150)),
                ('biaya', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siswa.biaya')),
                ('nama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siswa.siswa')),
            ],
            options={
                'verbose_name_plural': 'Pembayaran',
            },
        ),
        migrations.CreateModel(
            name='Pelanggaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelanggaran', models.CharField(blank=True, max_length=200, null=True)),
                ('kategory', models.CharField(blank=True, choices=[('Ringan', 'Ringan'), ('Sedang', 'Sedang'), ('Berat', 'Berat')], max_length=150)),
                ('kejadian', models.DateField()),
                ('keterangan', models.CharField(blank=True, max_length=200)),
                ('hukuman', models.CharField(blank=True, max_length=150)),
                ('nama_santri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='siswa.siswa')),
            ],
            options={
                'verbose_name_plural': 'Laporan Pelanggaran',
            },
        ),
    ]

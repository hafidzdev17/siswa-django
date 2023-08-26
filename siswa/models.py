from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Kelas(models.Model):

    STATUS_CHOICES = (
        ('Aktif', 'Aktif'),
        ('Nonaktif', 'Nonaktif'),
    )

    nama_kelas = models.CharField(max_length=10)
    status_kelas = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Aktif')
    
    def __str__(self):
        return self.nama_kelas

    class Meta:
        verbose_name_plural ="Kelas" 

class Siswa(models.Model):

    GENDER_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )

    INDIKATOR = (
        ('Iya', 'Iya'),
        ('Tidak', 'Tidak'),
    )

    STATUS = (
        ('Teratasi', 'Teratasi'),
        ('Sedang Diatasi', 'Sedang Diatasi'),
    )
    
    nama = models.CharField(max_length=200, blank=False, null=False)
    ttl = models.DateField(auto_now=False, auto_now_add=False)
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, default='L')
    berat_badan = models.CharField(max_length=10, unique = True, null=False)
    tinggi_badan = models.CharField(max_length=10, unique = True, null=False)
    tgl_operasi = models.DateField(auto_now=True, auto_now_add=False)
    indikator = models.CharField(max_length=20, choices=INDIKATOR, default='Iya')
    status = models.CharField(max_length=20, choices=STATUS, default='Teratasi')

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Siswa"

class Anak(models.Model):

    GENDER_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )

    INDIKATOR = (
        ('Iya', 'Iya'),
        ('Tidak', 'Tidak'),
    )

    STATUS = (
        ('Teratasi', 'Teratasi'),
        ('Sedang Diatasi', 'Sedang Diatasi'),
    )
    
    nama = models.CharField(max_length=200, blank=False, null=False)
    ttl = models.DateField(auto_now=False, auto_now_add=False)
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, default='L')
    berat_badan = models.CharField(max_length=10, unique = False, null=False)
    tinggi_badan = models.CharField(max_length=10, unique = False, null=False)
    tanggal_operasi = models.DateField(auto_now=False, auto_now_add=False)
    indikator = models.CharField(max_length=20, choices=INDIKATOR, default='Iya')
    status = models.CharField(max_length=20, choices=STATUS, default='Teratasi')
    posyandu = models.ForeignKey(Kelas, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Anak"

class Pembayaran(models.Model):

    Category = (
        ('KMS', 'KMS'),
        ('LKS', 'LKS'),
        ('Komputer', 'Komputer'),
    )

    Keterangan = (
        ('Lunas', 'Lunas'),
        ('Belum Lunas', 'Belum Lunas'),
    )

    nama = models.ForeignKey(Siswa, blank=False, null=True, on_delete=models.SET_NULL)
    pembayaran = models.CharField(max_length=100)
    biaya = models.CharField(max_length=100)
    tahun = models.CharField(max_length=100)
    kategori = models.CharField(max_length=150, blank=True, null=False, choices=Category)
    tanggal = models.DateField(auto_now=False, auto_now_add=False)
    keterangan = models.CharField(max_length=150, blank=True, null=False, choices=Keterangan)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Pembayaran"

class Petugas(models.Model):

    STATUS_CHOICES = (
        ('Aktif', 'Aktif'),
        ('Nonaktif', 'Nonaktif'),
    )

    user = models.OneToOneField(User, blank =True, null=True, on_delete = models.CASCADE)
    nama_petugas = models.CharField(max_length=200, blank=True, null=False)
    email = models.CharField(max_length=100,blank=True, unique = True, null=False)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Aktif')
    no_telpon = models.CharField(max_length=200, blank=True,  unique = True, null=False)

    def __str__(self):
        return self.nama_petugas
    class Meta:
        verbose_name_plural = "Petugas"

    
class Pelanggaran(models.Model):
    Category = (
        ('Ringan', 'Ringan'),
        ('Sedang', 'Sedang'),
        ('Berat', 'Berat'),
    )

    # Status = (
    #     ('Proses', 'Proses'),
    #     ('Selesai', 'Selesai'),
    # )
    nama_santri = models.ForeignKey(Siswa, blank=True, null=True, on_delete=models.SET_NULL)
    nama_pelanggaran = models.CharField(max_length=200, blank=True, null=True)
    kategory = models.CharField(max_length=150, blank=True, null=False, choices=Category)
    kejadian = models.DateField(blank=False, null=False)
    keterangan = models.CharField(max_length=200, blank=True, null=False)
    hukuman = models.CharField(max_length=150, blank=True, null=False)

    def __str__(self):
        return "%s" %(self.nama_santri)
        # return self.nama_santri
    class Meta:
        verbose_name_plural = "Laporan Pelanggaran"


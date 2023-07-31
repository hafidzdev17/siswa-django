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
    
    nisn = models.CharField(max_length=10, unique = True, null=False)
    nama = models.CharField(max_length=200, blank=False, null=False)
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, default='L')
    alamat = models.CharField(max_length=200, blank=True, null=True)
    ttl = models.DateField(auto_now=False, auto_now_add=False)
    tahun_akademik = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank=True)
    kelas = models.ForeignKey(Kelas, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Siswa"

class Pembayaran(models.Model):
    nama = models.ForeignKey(Siswa, blank=False, null=True, on_delete=models.SET_NULL)
    pembayaran = models.CharField(max_length=100)
    biaya = models.CharField(max_length=100)
    tahun = models.CharField(max_length=100)
    kelas = models.ForeignKey(Kelas, blank=False, null=True, on_delete=models.SET_NULL)

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


class RincianPembayaran(models.Model):

    Category = (
        ('KMS', 'KMS'),
        ('LKS', 'LKS'),
        ('Komputer', 'Komputer'),
    )

    Keterangan = (
        ('Lunas', 'Lunas'),
        ('Belum Lunas', 'Belum Lunas'),
    )
    
    nama_siswa = models.ForeignKey(Siswa, blank=False, null=True, on_delete=models.SET_NULL)
    kelas = models.ForeignKey(Kelas, blank=False, null=True, on_delete=models.SET_NULL)
    kategori = models.CharField(max_length=150, blank=True, null=False, choices=Category)
    tanggal = models.DateField(auto_now=False, auto_now_add=False)
    biaya = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=150, blank=True, null=False, choices=Keterangan)
    
    def __str__(self):
        return "%s" %(self.nama_siswa)

    class Meta:
        verbose_name_plural = "Rincian Pembayaran"

    
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


from django import forms
from django.forms import ModelForm, DateTimeInput
from .models import *

class KelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields= '__all__'
    
        widgets = {
            'nama_kelas': forms.TextInput(attrs={'class': 'form-select'}),
            'status_kelas': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nama_kelas' : 'Nama Kelas',
            'status_kelas': 'Status Kelas',
        }

class SiswaForm(ModelForm):
    class Meta:
        model = Siswa
        fields= '__all__'
    
        widgets = {
            'kelas': forms.Select(attrs={'class': 'form-select'}),
            'nama': forms.TextInput(attrs={'class': 'form-select'}),
            'jenis_kelamin': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'nisn': forms.TextInput(attrs={'class': 'form-select'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'ttl': forms.DateInput(format = '%m-%d-%Y',attrs={'type': 'date'}),
            'tahun_akademik': forms.TextInput(attrs={'class': 'form-select'}),
        }
        labels = {
            'kelas': 'Kelas',
            'nama' : 'Nama Lengkap',
            'jenis_kelamin' : 'Jenis Kelamin',
            'nisn': 'NISN',
            'alamat' : 'Alamat',
            'ttl': 'Tanggal lahir',
            'tahun_akademik' : 'Tahun Akademik',
        }

class PetugasForm(ModelForm):

    class Meta:
        model = Petugas
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'status': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nama_petugas' : 'Nama Petugas',
            'no_telpon' : 'Nomer telepon',
        }

class PembayaranForm(ModelForm):
    class Meta:
        model = Pembayaran
        fields= '__all__'
    
        widgets = {
            'nama': forms.Select(attrs={'class': 'form-select'}),
            'pembayaran': forms.TextInput(attrs={'class': 'form-select'}),
            'kategori': forms.Select(attrs={'class': 'form-select'}),
            'tanggal': forms.DateInput(format = '%m-%d-%Y',attrs={'type': 'date'}),
            'biaya': forms.TextInput(attrs={'class': 'form-control'}),
            'tahun': forms.TextInput(attrs={'class': 'form-select'}),
            'keterangan': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nama' : 'Nama Siswa',
            'pembayaran': 'Pembayaran',
            'kategori': 'Kategori Pembayaran',
            'tanggal' : 'Tanggal Pembayaran',
            'biaya' : 'Biaya',
            'tahun' : 'Tahun',
            'keterangan' : 'Keterangan',
        }

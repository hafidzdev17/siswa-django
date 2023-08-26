from django import forms
from django.forms import ModelForm, DateTimeInput
from .models import *
from dal import autocomplete

class KelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields= '__all__'
    
        widgets = {
            'nama_kelas': forms.TextInput(attrs={'class': 'form-select'}),
            'status_kelas': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nama_kelas' : 'Nama Posyandu',
            'status_kelas': 'Status',
        }

class AnakForm(ModelForm):
    class Meta:
        model = Anak
        fields= '__all__'
    
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-select'}),
            'ttl': forms.DateInput(attrs={'type': 'date'}),
            'jenis_kelamin': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'tanggal_operasi': forms.DateInput(attrs={'type': 'date'}),
            'berat_badan': forms.TextInput(attrs={'class': 'form-select'}),
            'tinggi_badan': forms.TextInput(attrs={'class': 'form-select'}),
            'indikator': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'posyandu': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nama' : 'Nama Lengkap',
            'ttl': 'Tanggal lahir',
            'jenis_kelamin' : 'Jenis Kelamin',
            'berat_badan': 'Berat Badan',
            'tinggi_badan': 'Tinggi Badan',
            'tanggal_operasi': 'Tanggal Operasi',
            'indikator' : 'Indikator',
            'status' : 'Status',
            'posyandu' : 'Posyandu',
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
            'nama_petugas' : 'Nama Admin',
            'no_telpon' : 'Nomer telepon',
        }

class PembayaranForm(forms.ModelForm):
  
    
    class Meta:
        model = Pembayaran
        fields = '__all__'
    
        widgets = {
            'nama': autocomplete.ModelSelect2(url='autocomplete'),
            'pembayaran': forms.TextInput(attrs={'class': 'form-select'}),
            'kategori': forms.Select(attrs={'class': 'form-select'}),
            'tanggal': forms.DateInput(format='%m-%d-%Y', attrs={'type': 'date'}),
            'biaya': forms.TextInput(attrs={'class': 'form-control'}),
            'tahun': forms.TextInput(attrs={'class': 'form-select'}),
            'keterangan': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nama': 'Nama Siswa',
            'pembayaran': 'Pembayaran',
            'kategori': 'Kategori Pembayaran',
            'tanggal': 'Tanggal Pembayaran',
            'biaya': 'Biaya',
            'tahun': 'Tahun',
            'keterangan': 'Keterangan',
        }
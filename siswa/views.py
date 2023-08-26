import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http import HttpResponse
from .filters import KelasFilter, SiswaFilter, PembayaranFilter
from .resource import PembayaranResource
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .decorators import tolakhalaman_ini
from django.contrib.auth.decorators import login_required
from dal import autocomplete
# Create your views here.

class SiswaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Siswa.objects.none()

        qs = Siswa.objects.all()

        if self.q:
            qs = qs.filter(nama__istartswith=self.q)

        return qs

class BiayaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Biaya.objects.none()

        qs = Biaya.objects.all()

        if self.q:
            qs = qs.filter(biaya__istartswith=self.q)

        return qs

def getfoto(request):
    santri = Santri.objects.get(id=request.GET.get('pk'))
    foto = santri.foto.name
    return HttpResponse(foto)

def telegram_bot(chat_id, message):
    # https://api.telegram.org/bot1837414090:AAEd-MMi0Z_NYxkHdNsQTbMNyhndwQCJycY/getUpdates
    bot_token = '1837414090:AAH5AB4hR_oX1xbDMsPs7F5N0RsimoLkFCY'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(send_text)
    return response.json()

# @ijinkan_pengguna(yang_diizinkan=['admin']) 
# @login_required(login_url='login')
def export_xls(request):
    pln = PembayaranResource()
    dataset = pln.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=pelangaran.xls'
    return response


@login_required
def beranda(request):
    
    pembayaran = Pembayaran.objects.all()
    total_kms =  pembayaran.filter(kategori='KMS').count()
    total_lks = pembayaran.filter(kategori='LKS').count()
    total_komputer = pembayaran.filter(kategori='Komputer').count()
    total_siswa = Siswa.objects.count()
    total_kelas = Kelas.objects.count()
    total_petugas = Petugas.objects.count()
    total_pembayaran = Pembayaran.objects.count()
  
    context = {
        'menu' : 'Beranda',
        'page' : 'Selamat Datang Di Beranda',
        'kms': total_kms,
        'lks': total_lks,
        'komputer': total_komputer,
        'siswa' : total_siswa,
        'kelas' : total_kelas,
        'petugas' : total_petugas,
        'pembayaran' : total_pembayaran,
    }
    return render(request, 'data/beranda.html', context)


@tolakhalaman_ini
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')
        else:
            messages.error(request, f"username/password salah")
            return redirect('login')
        
    context = {
        'menu': 'login',
        'page': 'Halaman Login',
        
    }
    return render(request, 'data/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


# views kelas
@login_required
def kelas(request):
    kelas_data = Kelas.objects.all()
    context = {
        'menu' : 'Form Kelas',
        'page' : 'Halaman Kelas',
        'kelas' : kelas_data,
        'filter_kelas' : KelasFilter
    }
    return render(request, 'data/kelas.html', context)

@login_required
def create_kelas(request):
    form = KelasForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kelas berhasil ditambahkan.')
        return redirect('kelas')
    context = {
        'menu' : 'Tambah Kelas',
        'page' : 'Halaman Tambah Kelas',
        'form': form
    }
    return render(request, 'data/kelas_form.html', context)

@login_required
def update_kelas(request, pk):
    kelas = Kelas.objects.get(id=pk)
    form = KelasForm(request.POST or None, request.FILES or None, instance=kelas)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kelas berhasil diupdate.')
        return redirect('kelas')
    context = {
        'menu' : 'Edit Kelas',
        'page' : 'Halaman Edit Kelas',
        'form': form
    }
    return render(request, 'data/kelas_form.html', context)

@login_required
def delete_kelas(request, pk):
    kelas = Kelas.objects.get(id=pk)
    if request.method == 'POST':
        kelas.delete()
        messages.success(request, 'Kelas berhasil dihapus.')
        return redirect('kelas')
    context = {
        'menu':'Menu Delete Kelas',
        'page':'Halaman Delete Kelas',
        'kelas': kelas
    }
    return render(request, 'data/kelas_delete.html', context)


# views siswa
@login_required
def siswa(request):
    siswa_data = Siswa.objects.order_by('-id')
    context = {
        'menu' : 'Form Siswa',
        'page' : 'Halaman Siswa',
        'siswa' : siswa_data,
        'filter_siswa' : SiswaFilter
    }
    return render(request, 'data/siswa.html', context)

@login_required
def create_siswa(request):
    form = SiswaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Siswa Berhasil Ditambahkan.')
        return redirect('siswa')
    context = {
        'menu' : 'Tambah Siswa',
        'page' : 'Halaman Tambah Siswa',
        'form': form
    }
    return render(request, 'data/siswa_form.html', context)


@login_required
def update_siswa(request, pk):
    siswa = Siswa.objects.get(id=pk)
    form = SiswaForm(request.POST or None, request.FILES or None, instance=siswa)
    if form.is_valid():
        form.save()
        messages.success(request, 'Siswa berhasil diupdate.')
        return redirect('siswa')
    context = {
        'menu' : 'Edit Siswa',
        'page' : 'Halaman Edit Siswa',
        'form': form
    }
    return render(request, 'data/siswa_form.html', context)

@login_required
def delete_siswa(request, pk):
    siswa = Siswa.objects.get(id=pk)
    if request.method == 'POST':
        siswa.delete()
        messages.success(request, 'Siswa berhasil dihapus.')
        return redirect('siswa')
    context = {
        'menu':'Menu Delete Siswa',
        'page':'Halaman Delete Siswa',
        'siswa': siswa
    }
    return render(request, 'data/siswa_delete.html', context)

@login_required
# petugas
def petugas(request):
    data = Petugas.objects.order_by('-id')
    context ={
        "menu" : 'Petugas',
        "page" : 'Halaman Petugas',
        'petugas' : data
    }
    return render(request, 'data/petugas.html', context)

@login_required
def create_petugas(request):
    form = PetugasForm()
    petugas = PetugasForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada.')
            return redirect('create_petugas')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('create_petugas')
        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()

        # Petugas
        createPetugas = petugas.save()
        createPetugas.user = user
        createPetugas.save()
        messages.success(request, 'petugas berhasil ditambahkan.')
        
        return redirect('petugas')

    context ={
        "menu" : 'Input Petugas',
        "page" : 'Halaman Petugas',
        "form" : form
        
    }
    return render(request, 'data/petugas_form.html', context)

@login_required
def delete_petugas(request, pk):
    delete_petugas = Petugas.objects.get(id=pk)
    if request.method == 'POST':
        delete_petugas.delete()
        messages.success(request, 'petugas berhasil dihapus.')
        return redirect ('petugas')
    context = {
        'menu':'Menu Delete Petugas',
        'page':'Halaman Delete Petugas',
        'petugas': delete_petugas
    }
    return render(request, 'data/petugas_delete.html', context)


# pembayaran

@login_required
def pembayaran(request):
    siswa_data = Siswa.objects.order_by('-id')
    pembayaran_data = Pembayaran.objects.order_by('-id')
    context = {
        'menu' : 'Form Pembayaran',
        'page' : 'Halaman Pembayaran',
        'pembayaran' : pembayaran_data,
        'siswa': siswa_data
    }
    return render(request, 'data/pembayaran.html', context)


@login_required
def create_pembayaran(request):
    form = PembayaranForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'pembayaran berhasil ditambahkan.')
        return redirect('pembayaran')
    context = {
        'menu' : 'Tambah Pembayaran',
        'page' : 'Halaman Tambah Pembayaran',
        'form': form
    }
    return render(request, 'data/pembayaran_form.html', context)

@login_required
def update_pembayaran(request, pk):
    pembayaran = Pembayaran.objects.get(id=pk)
    form = PembayaranForm(request.POST or None, request.FILES or None, instance=pembayaran)
    if form.is_valid():
        form.save()
        messages.success(request, 'pembayaran berhasil diupdate.')
        return redirect('pembayaran')
    context = {
        'menu' : 'Edit Pembayaran',
        'page' : 'Halaman Edit Pembayaran',
        'form': form
    }
    return render(request, 'data/pembayaran_form.html', context)

@login_required
def delete_pembayaran(request, pk):
    pembayaran = Pembayaran.objects.get(id=pk)
    nama_siswa = pembayaran.nama.nama

    if request.method == 'POST':
        pembayaran.delete()
        messages.success(request, 'pembayaran berhasil dihapus.')
        return redirect('pembayaran')
        
    context = {
        'menu':'Menu Delete Pembayaran',
        'page':'Halaman Delete Pembayaran',
        'nama_siswa': nama_siswa
    }
    return render(request, 'data/pembayaran_delete.html', context)


# @ijinkan_pengguna(yang_diizinkan=['admin']) 
# @login_required(login_url='login')
def pelanggaran(request):
    namaPelanggaran = Pelanggaran.objects.order_by('-id')
    context = {
        'menu' : 'pelanggaran',
        'page' : 'Halaman pelanggaran',
        'formpelanggaran' : namaPelanggaran,
    }
    return render(request, 'data/pelanggaran.html', context)

# @ijinkan_pengguna(yang_diizinkan=['admin']) 
# @login_required(login_url='login')
def inputpelanggaran(request):
    formpelanggaran = PelanggaranForm()
    if request.method =='POST':
        formsimpan = PelanggaranForm(request.POST)
        if formsimpan.is_valid:
            santri = formsimpan['nama_santri'].value()
            pelanggaran = formsimpan['nama_pelanggaran'].value()
            hukuman = formsimpan['hukuman'].value()
            datasantri = Santri.objects.get(id=santri)
            chat_id = datasantri.nama_wali.chat_id

            pesan = f'INFORMASI PELANGGARAN!\nkepada bapak/ibu {datasantri.nama_wali}. ananda {datasantri.nama} teridentifikasi melakukan pelanggaran {pelanggaran} dengan hukuman {hukuman}'
            formsimpan.save()

            msg = 'Berhasil menambahkan data pelanggaran!'
            if chat_id is not None :
                telegram_bot(chat_id, pesan)
                msg += ' dan mengirimkan detail kepada telegram wali santri.'

            messages.success(request, f'{msg}')
            return redirect('pelanggaran')
    context = {
        'menu' : 'input santri',
        'page' : 'Halaman Input Santri',
        'formpln': formpelanggaran
    }
    return render(request,'data/inputpelanggaran.html', context)

# @ijinkan_pengguna(yang_diizinkan=['admin']) 
# @login_required(login_url='login')
def updatePelanggaran(request, pk):
	pelanggaranupdate = Pelanggaran.objects.get(id=pk)
	formpelanggaran = PelanggaranForm(instance=pelanggaranupdate)
	if request.method == 'POST':
		formedit = PelanggaranForm(request.POST, instance=pelanggaranupdate)
		if formedit.is_valid:
			formedit.save()
			return redirect('pelanggaran')
	context = {
		'menu': 'Edit pelanggaran',
        'page': 'Halaman update pelanggaran',
		'formpln': formpelanggaran
	}
	return render(request, 'data/inputpelanggaran.html', context)

# @ijinkan_pengguna(yang_diizinkan=['admin']) 
# @login_required(login_url='login')
def deletePelanggaran(request, pk):
    pelanggaranhapus = Pelanggaran.objects.get(id=pk)
    if request.method == 'POST':
        pelanggaranhapus.delete()
        messages.success(request, f'Data pelanggaran berhasil dihapus!')
        return redirect ('pelanggaran')
    context = {
        'menu':'menu delete pelanggaran',
        'page':'halaman delete pelanggaran',
        'formhapuspelanggaran': pelanggaranhapus
    }
    return render(request, 'data/delete_pelanggaran.html', context)


# @ijinkan_pengguna(yang_diizinkan=['pengurus']) 
# @login_required(login_url='login')
def pelanggaranuser(request):
    namaPelanggaran = Pelanggaran.objects.order_by('-id')
    context = {
        'menu' : 'pelanggaran',
        'page' : 'Halaman pelanggaran',
        'formpelanggaran' : namaPelanggaran
    }
    return render(request, 'userpage/pelanggaranuser.html', context)

# @ijinkan_pengguna(yang_diizinkan=['pengurus']) 
# @login_required(login_url='login')
def inputpelanggaranuser(request):
    formpelanggaran = PelanggaranForm()
    if request.method =='POST':
        formsimpan = PelanggaranForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pelanggaran')
    context = {
        'menu' : 'input santri',
        'page' : 'Halaman Input Santri',
        'formpln': formpelanggaran
    }
    return render(request,'userpage/inputpelanggaranuser.html', context)

def deletePelanggaranuser(request, pk):
    pelanggaranhapus = Pelanggaran.objects.get(id=pk)
    if request.method == 'POST':
        pelanggaranhapus.delete()
        return redirect ('pelanggaranuser')
    context = {
        'menu':'menu delete pelanggaran',
        'page':'halaman delete pelanggaran',
        'formhapuspelanggaran': pelanggaranhapus
    }
    return render(request, 'userpage/delete_pelanggaran_user.html', context)

def laporan(request):
    pembayaran = Pembayaran.objects.order_by('-id')
    filterpembayaran = PembayaranFilter(request.GET, queryset=pembayaran)
    filter_pel = filterpembayaran.qs
    context = {
        'menu' : 'laporan',
        'page' : 'Halaman Laporan',
        'filter_pln' : filterpembayaran,
        'pembayaran' : filter_pel,
    }
    return render(request, 'data/formlaporan.html', context)    

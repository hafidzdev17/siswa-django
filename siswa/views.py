import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http import HttpResponse
from .filters import KelasFilter, SiswaFilter, PelanggaranFilter
from .resource import PelanggaranResource
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
# Create your views here.


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
    pln = PelanggaranResource()
    dataset = pln.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=pelangaran.xls'
    return response

# @login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin']) 
# @pilihan_login
def beranda(request):
    list_pelanggaran = Pelanggaran.objects.all()
    ringan = list_pelanggaran.filter(kategory='Ringan').count()
    sedang = list_pelanggaran.filter(kategory='Sedang').count()
    berat = list_pelanggaran.filter(kategory='Berat').count()
    total = list_pelanggaran.count()
    context = {
        'menu' : 'Beranda',
        'page' : 'Selamat Datang Di Beranda',
        'plnringan' : ringan,
        'plnsedang' : sedang,
        'plnberat' : berat,
        'totalpln' : total

    }
    return render(request, 'data/beranda.html', context)

def registerPage(request):
    context = {
        'menu': 'register',
        'page': 'Halaman Register',
	
    }
    return render(request, 'data/register.html', context)

# @tolakhalaman_ini
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
def kelas(request):
    kelas_data = Kelas.objects.all()
    context = {
        'menu' : 'Form Kelas',
        'page' : 'Halaman Kelas',
        'kelas' : kelas_data,
        'filter_kelas' : KelasFilter
    }
    return render(request, 'data/kelas.html', context)

def create_kelas(request):
    form = KelasForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('kelas')
    context = {
        'menu' : 'Tambah Kelas',
        'page' : 'Halaman Tambah Kelas',
        'form': form
    }
    return render(request, 'data/kelas_form.html', context)

def update_kelas(request, pk):
    kelas = Kelas.objects.get(id=pk)
    form = KelasForm(request.POST or None, request.FILES or None, instance=kelas)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kelas berhasil ditambahkan.')
        return redirect('kelas')
    context = {
        'menu' : 'Edit Kelas',
        'page' : 'Halaman Edit Kelas',
        'form': form
    }
    return render(request, 'data/kelas_form.html', context)

def delete_kelas(request, pk):
    kelas = Kelas.objects.get(id=pk)
    if request.method == 'POST':
        kelas.delete()
        return redirect('kelas')
    context = {
        'menu':'Menu Delete Kelas',
        'page':'Halaman Delete Kelas',
        'kelas': kelas
    }
    return render(request, 'data/kelas_delete.html', context)


# views siswa
def siswa(request):
    siswa_data = Siswa.objects.all()
    context = {
        'menu' : 'Form Siswa',
        'page' : 'Halaman Siswa',
        'siswa' : siswa_data,
        'filter_siswa' : SiswaFilter
    }
    return render(request, 'data/siswa.html', context)


def create_siswa(request):
    form = SiswaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('siswa')
    context = {
        'menu' : 'Tambah Siswa',
        'page' : 'Halaman Tambah Siswa',
        'form': form
    }
    return render(request, 'data/siswa_form.html', context)

def update_siswa(request, pk):
    siswa = Siswa.objects.get(id=pk)
    form = SiswaForm(request.POST or None, request.FILES or None, instance=siswa)
    if form.is_valid():
        form.save()
        messages.success(request, 'Siswa berhasil ditambahkan.')
        return redirect('siswa')
    context = {
        'menu' : 'Edit Siswa',
        'page' : 'Halaman Edit Siswa',
        'form': form
    }
    return render(request, 'data/siswa_form.html', context)

def delete_siswa(request, pk):
    siswa = Siswa.objects.get(id=pk)
    if request.method == 'POST':
        siswa.delete()
        return redirect('siswa')
    context = {
        'menu':'Menu Delete Santri',
        'page':'Halaman Delete Santri',
        'siswa': siswa
    }
    return render(request, 'data/siswa_delete.html', context)


# petugas
def petugas(request):
    data = Petugas.objects.order_by('-id')
    context ={
        "menu" : 'Petugas',
        "page" : 'Halaman Petugas',
        'petugas' : data
    }
    return render(request, 'data/petugas.html', context)

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
        # user


        # Petugas
        createPetugas = petugas.save()
        createPetugas.user = user
        createPetugas.save()
        
        return redirect('petugas')

    context ={
        "menu" : 'Input Petugas',
        "page" : 'Halaman Petugas',
        "form" : form
        
    }
    return render(request, 'data/petugas_form.html', context)

def delete_petugas(request, pk):
    delete_petugas = Petugas.objects.get(id=pk)
    if request.method == 'POST':
        delete_petugas.delete()
        return redirect ('petugas')
    context = {
        'menu':'Menu Delete Petugas',
        'page':'Halaman Delete Petugas',
        'petugas': delete_petugas
    }
    return render(request, 'data/petugas_delete.html', context)

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
    pelanggaran = Pelanggaran.objects.all()
    filterpelanggaran = PelanggaranFilter(request.GET, queryset=pelanggaran)
    filter_pel = filterpelanggaran.qs
    context = {
        'menu' : 'laporan',
        'filter_pln' : filterpelanggaran,
        'pelanggaran' : filter_pel,
    }
    return render(request, 'data/formlaporan.html', context)    

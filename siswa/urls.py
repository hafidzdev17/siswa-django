from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .views import SiswaAutocomplete, BiayaAutocomplete

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('accounts/login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    # path('register/', views.registerPage, name='register'),

    # kelas
    path('kelas', views.kelas, name='kelas'),
    path('create_kelas/', views.create_kelas, name='create_kelas'),
    path('update_kelas/<int:pk>/', views.update_kelas, name='update_kelas'),
    path('delete_kelas/<int:pk>/', views.delete_kelas, name='delete_kelas'),

    # siswa
    path('siswa', views.siswa, name='siswa'),
    path('create_siswa/', views.create_siswa, name='create_siswa'),
    path('update_siswa/<int:pk>/', views.update_siswa, name='update_siswa'),
    path('delete_siswa/<int:pk>/', views.delete_siswa, name='delete_siswa'),

    # petugas
    path('petugas', views.petugas, name='petugas'),
    path('create_petugas', views.create_petugas, name='create_petugas'),
    path('delete_petugas/<str:pk>', views.delete_petugas, name='delete_petugas'),

    # pembayaran
    path('autocomplete/', SiswaAutocomplete.as_view(), name='autocomplete'),
    path('autocompletes/', BiayaAutocomplete.as_view(), name='autocompletes'),
    path('pembayaran', views.pembayaran, name='pembayaran'),
    path('create_pembayaran/', views.create_pembayaran, name='create_pembayaran'),
    path('update_pembayaran/<int:pk>/', views.update_pembayaran, name='update_pembayaran'),
    path('delete_pembayaran/<str:pk>/', views.delete_pembayaran, name='delete_pembayaran'),

    path('pelanggaran/', views.pelanggaran, name='pelanggaran'),
    path('inputpelanggaran/', views.inputpelanggaran, name='inputpelanggaran'),
    path('updatepelanggaran/<str:pk>', views.updatePelanggaran, name='updatepelanggaran'),
    path('deletepelanggaran/<str:pk>', views.deletePelanggaran, name='deletepelanggaran'),
  
    path('export/xls/', views.export_xls, name='export_xls'),
    path('pelanggaranuser/', views.pelanggaranuser, name='pelanggaranuser'),
    path('inputpelanggaranuser/', views.inputpelanggaranuser, name='inputpelanggaranuser'),
    path('deletepelanggaranuser/<str:pk>', views.deletePelanggaranuser, name='deletepelanggaranuser'),
    path('laporan/', views.laporan, name='laporan'),
    path('getfoto/', views.getfoto, name='getfoto'),
    # path('autocomplete/', views.autocomplete, name='autocomplete')

    # path('profil/<no_induk>', views.profil, name='profil'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
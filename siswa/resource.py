from import_export import resources
from .models import Pembayaran
from import_export.fields import Field

class PembayaranResource(resources.ModelResource):
    nama_siswa__nama = Field(attribute='nama_siswa', column_name='Nama Siswa')
    class Meta:
        model = Pembayaran
        fields = ['nama_siswa__nama', 'jumlah_pembayaran', 'biaya_pembayaran', 'kategori_pembayaran', 'tanggal_pembayaran','tahun','keterangan']


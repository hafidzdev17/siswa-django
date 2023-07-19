import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class KelasFilter(django_filters.FilterSet):
    nama_kelas = CharFilter(field_name="nama_kelas", lookup_expr='icontains')

    class Meta:
        model = Kelas
        fields = ['nama_kelas']

class SiswaFilter(django_filters.FilterSet):
    nama = CharFilter(field_name="nama", lookup_expr='icontains')

    class Meta:
        model = Siswa
        fields = ['nama']

class PelanggaranFilter(django_filters.FilterSet):
    tglmulai = DateFilter(field_name="kejadian", lookup_expr='gte')
    tglakhir = DateFilter(field_name="kejadian", lookup_expr='lte')

    class Meta:
        model = Pelanggaran
        fields ='__all__'
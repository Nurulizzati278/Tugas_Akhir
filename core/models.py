from django.db import models
from datetime import datetime

# Create your models here.


# class SuperAdmin(models.Model):
#     Operatorid = models.BigAutoField(primary_key=True)
#     NIP = models.AutoField(max_length=25)
#     Nama = models.CharField(max_length=250)
#     Divisi = models.CharField(max_length=250)
#     Ditambahkan = models.DateField(auto_now=True, null=True, blank=True)


# class AdminSekolah(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     NIP = models.BigAutoField(max_length=25)
#     Nama = models.CharField(max_length=250)
#     NamaSekolah = models.CharField(max_length=100)
#     Username = models.CharField(max_length=250)
#     Jabatan = models.CharField(max_length=100)
#     # Gambar = models.ImageField(upload_to=common,null=True, blank=True)
#     Ditambahkan = models.DateField(auto_now_add=True, null=True, blank=True)


# class PengajuanSekolah(models.Model):
#     PengajuanId = models.BigAutoField(primary_key=True)
#     TanggalAjukan = models.DateField(auto_now_add=True, null=True, blank=True)
#     NamaSekolah = models.CharField(max_length=250)
#     NamaKepalaSekolah = models.CharField(max_length=250)
#     NamaPengawasSekolah = models.CharField(max_length=250)
#     AlamatSekolah = models.CharField(max_length=500)


# class DataSekolah(models.Model):
#     SekolahId = models.BigAutoField(primary_key=True)
#     TanggalBerdiri = models.DateField(auto_now_add=True, null=True, blank=True)
#     JumlahPegawai = models.IntegerField(max_length=100)
#     JabatanKeseluruhan = models.IntegerField(max_length=100)
#     # Gambar = models.ImageField(upload_to=common, null=True, blank=True)


# class Akreditasi(models.Model):
#     AKREDITASI_CHOICES = (
#         ("A", "SANGAT BAIK"),
#         ("B", "BAIK"),
#         ("C", "CUKUP"),
#         ("TT", "TIDAK TERAKREDITASI"),
#     )
#     Akreditasiid = models.BigAutoField(primary_key=True)
#     StandarKompetensiLulusan = models.BigAutoField(max_length=100)
#     StandarIsi = models.BigAutoField(max_length=100)
#     StandarProses = models.BigAutoField(max_length=100)
#     StandarPendidikandanTenagaKependidikan = models.BigAutoField(max_length=100)
#     StandarSaranadanPrasarana = models.BigAutoField(max_length=100)
#     StandarPengelolaan = models.BigAutoField(max_length=100)
#     StandarPembiayaanPendidikan = models.BigAutoField(max_length=100)
#     StandarPenilaianPendidikan = models.BigAutoField(max_length=100)
#     StatusAkreditasi = models.CharField(max_length=50, choices=AKREDITASI_CHOICES)


# class Nilai(models.Model):
#     Nilaiid = models.BigAutoField(primary_key=True)
#     NamaNilai = models.CharField(max_length=50)
#     RangeNilai = models.BigAutoField(max_length=250)
#     Warna = models.CharField(max_length=50)


# class Location(models.Model):
#     LokasiId = models.BigAutoField(primary_key=True)
#     Latitude = models.FloatField(max_length=500)
#     Longtitude = models.FloatField(max_length=500)

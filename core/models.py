from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
import os
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, nip, nama, umur, golongan, password=None):
        if not nip:
            raise ValueError('NIP field must be set')
        user = self.model(
            nip=nip,
            nama=nama,
            umur=umur,
            golongan=golongan,
        )
        user.set_password(password)  # hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, nip, nama, umur, golongan, password=None):
        user = self.create_user(
            nip=nip,
            nama=nama,
            umur=umur,
            golongan=golongan,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    nip = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=255)
    umur = models.IntegerField()
    profil = models.ImageField(upload_to='profil/', null=True, blank=True)
    golongan = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="customuser_groups"  # Ubah related_name di sini
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="customuser_permissions"  # Ubah related_name di sini
    )
    
    objects = CustomUserManager()

    # Use NIP as the username field
    USERNAME_FIELD = 'nip'
    REQUIRED_FIELDS = ['nama', 'umur', 'golongan']

    def __str__(self):
        return self.nama

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser




   

# class AdminSekolah(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     NIP = models.BigAutoField(max_length=25)
#     Nama = models.CharField(max_length=250)
#     NamaSekolah = models.CharField(max_length=100)
#     Username = models.CharField(max_length=250)
#     Jabatan = models.CharField(max_length=100)
#     # Gambar = models.ImageField(upload_to=common,null=True, blank=True)
#     Ditambahkan = models.DateField(auto_now_add=True, null=True, blank=True)



# udah diperbaiki belum di migrate
class PengajuanSekolah(models.Model):
    PengajuanId = models.BigAutoField(primary_key=True)
    TanggalAjukan = models.DateField(auto_now_add=True, null=True, blank=True)
    NamaSekolah = models.CharField(max_length=250)
    NamaKepalaSekolah = models.CharField(max_length=250)
    NamaPengawasSekolah = models.CharField(max_length=250)
    AlamatSekolah = models.CharField(max_length=500)
    data_sekolah = models.OneToOneField('DataSekolah', on_delete=models.CASCADE)
    akreditasi = models.OneToOneField('Akreditasi', on_delete=models.CASCADE)
    def __str__(self):
        return self.NamaSekolah

class DataSekolah(models.Model):
    SekolahId = models.BigAutoField(primary_key=True)
    TanggalBerdiri = models.DateField(null=True, blank=True)
    JumlahPegawai = models.CharField(max_length=250)
    JabatanKeseluruhan = models.IntegerField()

class Akreditasi(models.Model):
    AKREDITASI_CHOICES = (
        ("A", "SANGAT BAIK"),
        ("B", "BAIK"),
        ("C", "CUKUP"),
        ("TT", "TIDAK TERAKREDITASI"),
    )
    Akreditasiid = models.BigAutoField(primary_key=True)
    StandarKompetensiLulusan = models.CharField(max_length=100)
    StandarIsi = models.CharField(max_length=100)
    StandarProses = models.CharField(max_length=100)
    StandarPendidikandanTenagaKependidikan = models.CharField(max_length=100)
    StandarSaranadanPrasarana = models.CharField(max_length=100)
    StandarPengelolaan = models.CharField(max_length=100)
    StandarPembiayaanPendidikan = models.CharField(max_length=100)
    StandarPenilaianPendidikan = models.CharField(max_length=100)
    StatusAkreditasi = models.CharField(max_length=50, choices=AKREDITASI_CHOICES)

class Nilai(models.Model):
    Nilaiid = models.BigAutoField(primary_key=True)
    NamaNilai = models.CharField(max_length=50)
    RangeNilai = models.CharField(max_length=250)
    Warna = models.CharField(max_length=50)

class Location(models.Model):
    LokasiId = models.BigAutoField(primary_key=True)
    Latitude = models.FloatField()
    Longtitude = models.FloatField()
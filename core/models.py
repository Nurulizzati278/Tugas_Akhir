from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models

import os
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, nip, nama, umur, golongan, password=None):
        if not nip:
            raise ValueError("NIP field must be set")
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
    profil = models.ImageField(upload_to="profil/", null=True, blank=True)
    golongan = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="customuser_groups",  # Ubah related_name di sini
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="customuser_permissions",  # Ubah related_name di sini
    )

    objects = CustomUserManager()

    # Use NIP as the username field
    USERNAME_FIELD = "nip"
    REQUIRED_FIELDS = ["nama", "umur", "golongan"]

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


def GambarSekolah(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"GambarSekolah/{unique_filename}"


class PengajuanSekolah(models.Model):
    AKREDITASI_CHOICES = (
        ("A", "SANGAT BAIK"),
        ("B", "BAIK"),
        ("C", "CUKUP"),
        ("TT", "TIDAK TERAKREDITASI"),
    )
    SekolahId = models.BigAutoField(primary_key=True)
    GambarSekolah = models.ImageField(upload_to=GambarSekolah, null=True, blank=True)
    TanggalAjukan = models.DateField(auto_now_add=True, null=True, blank=True)
    NamaSekolah = models.CharField(max_length=250)
    NamaKepalaSekolah = models.CharField(max_length=250)
    NamaPengawasSekolah = models.CharField(max_length=250)
    AlamatSekolah = models.CharField(max_length=500)
    JumlahGuruPNS = models.IntegerField(null=True, blank=True)
    JumlahGuruHonorer = models.IntegerField(null=True, blank=True)
    JumlahStaf = models.IntegerField(null=True, blank=True)
    JumlahSiswaX = models.IntegerField(null=True, blank=True)
    JumlahSiswaXI = models.IntegerField(null=True, blank=True)
    JumlahSiswaXII = models.IntegerField(null=True, blank=True)
    JumlahRuangKelas = models.IntegerField(null=True, blank=True)
    StatusAkreditasi = models.CharField(max_length=50, choices=AKREDITASI_CHOICES)

# Upload Komponen Mutu Lulusan
def LaporanJadwalKegiatan(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanJadwalKegiatan/{unique_filename}"

def TataTertib(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"TataTertib/{unique_filename}"

def LaporanKegiatanProgramKreatif(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanKegiatanProgramKreatif/{unique_filename}"

def LaporanHasilKaryaPrestasi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanHasilKaryaPrestasi/{unique_filename}"

def BuktiKegiatanEkstrakulikuler(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"BuktiKegiatanEkstrakulikuler/{unique_filename}"

def BuktiKegiatanOsis(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"BuktiKegiatanOsis/{unique_filename}"

def BuktiKegiatanDenganPihakLuar(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"BuktiKegiatanDenganPihakLuar/{unique_filename}"

def Sertifikat(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"Sertifikat/{unique_filename}"

def PortofolioTugasSiswa(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"PortofolioTugasSiswa/{unique_filename}"

def PortofolioTugasMateriPengembangan(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"PortofolioTugasMateriPengembangan/{unique_filename}"

def LaporanPrestasiSiswaLomba(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanPrestasiSiswaLomba/{unique_filename}"

def DataNilaiUjian(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DataNilaiUjian/{unique_filename}"

def LaporanHasilTracerStudy(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanHasilTracerStudy/{unique_filename}"

#def LaporanKegiatanProgramKreatif(instance, filename):
#    _, file_extension = os.path.splitext(filename)
#    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
#    return f"LaporanKegiatanProgramKreatif/{unique_filename}"

def KomponenMutuLulusan(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"KomponenMutuLulusan/{unique_filename}"

# Upload file komponen proses pembelajaran
def LembarKerjaSiswa(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LembarKerjaSiswa/{unique_filename}"

def KisiKisiSoalInstrumenHasilPenilaian(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"KisiKisiSoalInstrumenHasilPenilaian/{unique_filename}"

def AnalisisPencapaianKompetensi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"AnalisisPencapaianKompetensi/{unique_filename}"

def JadwalRemedial(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"JadwalRemedial/{unique_filename}"

def RKS4Tahun(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"RKS4Tahun/{unique_filename}"

def RKAS1Tahun(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"RKAS1Tahun/{unique_filename}"

def DaftarPenggunaanSapras(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DaftarPenggunaanSapras/{unique_filename}"

def RPP(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"RPP/{unique_filename}"

#def LembarKerjaSiswa(instance, filename):
#    _, file_extension = os.path.splitext(filename)
#    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
#    return f"LembarKerjaSiswa/{unique_filename}"

def KomponenProsesPembelajaran(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"KomponenProsesPembelajaran/{unique_filename}"

# Upload file komponen mutu guru
def RPP(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"RPP/{unique_filename}"

def LaporanEvaluasi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanEvaluasi/{unique_filename}"

def LaporanDariSiswa(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanDariSiswa/{unique_filename}"

def LaporanDariGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanDariGuru/{unique_filename}"

def BuktiDaftarHadir(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"BuktiDaftarHadir/{unique_filename}"

def LaporanPengembanganGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanPengembanganGuru/{unique_filename}"

def LaporanKegiatanDiseminasi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanKegiatanDiseminasi/{unique_filename}"

#def LembarKerjaSiswa(instance, filename):
#    _, file_extension = os.path.splitext(filename)
#    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
#    return f"LembarKerjaSiswa/{unique_filename}"

def KomponenMutuGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"KomponenMutuGuru/{unique_filename}"


# Upload file komponen manajemen sekolah
def DaftarHadirRapatVisiMisi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DaftarHadirRapatVisiMisi/{unique_filename}"

def LaporanKegiatanImplementasiVisiMisi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanKegiatanImplementasiVisiMisi/{unique_filename}"

def DokumenHasilEvaluasi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenHasilEvaluasi/{unique_filename}"

def DokumenRekomendasi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenRekomendasi/{unique_filename}"

def DokumenVisiMisiSebelumnyaDanSetelah(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenVisiMisiSebelumnyaDanSetelah/{unique_filename}"

def JadwalSupervisi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"JadwalSupervisi/{unique_filename}"

def DokumenHasilObservasiKepsek(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenHasilObservasiKepsek/{unique_filename}"

def DaftarHadirRapatRKSRKASdanNotulen(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DaftarHadirRapatRKSRKASdanNotulen/{unique_filename}"

def LaporanKegiatanPelaksanaanProgram(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanKegiatanPelaksanaanProgram/{unique_filename}"

def DokumenKerjaSama(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenKerjaSama/{unique_filename}"

def DokumenPelaksanaanKegiatanKebersihan(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenPelaksanaanKegiatanKebersihan/{unique_filename}"

def DokumenRKAS1Tahun(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenRKAS1Tahun/{unique_filename}"

def DokumenRKAS4Tahun(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenRKAS4Tahun/{unique_filename}"

def DaftarHadirRapatRKSRKASdanNotulen(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DaftarHadirRapatRKSRKASdanNotulen/{unique_filename}"

def RPP(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"RPP/{unique_filename}"

def NotulenRakerKurikulum(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"NotulenRakerKurikulum/{unique_filename}"

def DokumenRakerEvaluasiKurikulum(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenRakerEvaluasiKurikulum/{unique_filename}"

def SOPPelaksanaanTugasGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"SOPPelaksanaanTugasGuru/{unique_filename}"

def JadwalMengajarGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"JadwalMengajarGuru/{unique_filename}"

def DokumenPenilaianKriteriaGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenPenilaianKriteriaGuru/{unique_filename}"

def HasilPenilaianKinerjaGuru(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"HasilPenilaianKinerjaGuru/{unique_filename}"

def DokumenPenilaianKinerjaTendik(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenPenilaianKinerjaTendik/{unique_filename}"

def HasilPenilaianKinerjaTendik(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"HasilPenilaianKinerjaTendik/{unique_filename}"

def BuktiSaksiAtauPenghargaan(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"BuktiSaksiAtauPenghargaan/{unique_filename}"

def SOPPengelolaanSapras(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"SOPPengelolaanSapras/{unique_filename}"

def DokumenRapatPenyususanRAPBS(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenRapatPenyususanRAPBS/{unique_filename}"

def RAPBS(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"RAPBS/{unique_filename}"

def LaporanKeuangan1TahunTerakhir(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"LaporanKeuangan1TahunTerakhir/{unique_filename}"

def HasilCatatanAuditInternelEksternal3TahunTerakhir(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"HasilCatatanAuditInternelEksternal3TahunTerakhir/{unique_filename}"

def DokumenProgramEkstrakulikuler(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenProgramEkstrakulikuler/{unique_filename}"

def SuratTugasPembinaDanTimLomba(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"SuratTugasPembinaDanTimLomba/{unique_filename}"

def SertifikatPrestasi(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"SertifikatPrestasi/{unique_filename}"

def DokumenProgramLayananBK(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenProgramLayananBK/{unique_filename}"

def DokumenRKATahunSebelumnya(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenRKATahunSebelumnya/{unique_filename}"

def DokumenEvaluasiDiriTahunSebelumnya(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"DokumenEvaluasiDiriTahunSebelumnya/{unique_filename}"

def KomponenManajemenSekolah(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"KomponenManajemenSekolah/{unique_filename}"

class PengajuanAkreditasi(models.Model):
    KEBUTUHAN_CHOICES = (
        ("ADA", "ADA"),
        ("tIDAK ADA", "TIDAK ADA"),
    )
    AkreditasiId = models.BigAutoField(primary_key=True)
    SekolahId = models.ForeignKey(PengajuanSekolah, on_delete=models.CASCADE)
    # Komponen Mutu Lulusan
    TataTertib = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarTataTertib = models.ImageField(upload_to=TataTertib, null=True, blank=True)
    LaporanJadwalKegiatan = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanJadwalKegiatan = models.ImageField(upload_to=LaporanJadwalKegiatan, null=True, blank=True)
    TataTertib = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambartataTertib = models.ImageField(upload_to=TataTertib, null=True, blank=True)
    LaporanKegiatanProgramKreatif = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanKegiatanProgramKreatif = models.ImageField(upload_to=LaporanKegiatanProgramKreatif, null=True, blank=True)
    LaporanHasilKaryaPrestasi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanHasilKaryaPrestasi = models.ImageField(upload_to=LaporanHasilKaryaPrestasi, null=True, blank=True)
    BuktiKegiatanEkstrakulikuler = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarBuktiKegiatanEkstrakulikuler = models.ImageField(upload_to=BuktiKegiatanEkstrakulikuler, null=True, blank=True)
    BuktiKegiatanOsis = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarBuktiKegiatanOsis = models.ImageField(upload_to=BuktiKegiatanOsis, null=True, blank=True)
    BuktiKegiatanDenganPihakLuar = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarBuktiKegiatanDenganPihakLuar = models.ImageField(upload_to=BuktiKegiatanDenganPihakLuar, null=True, blank=True)
    Sertifikat = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarSertifikat = models.ImageField(upload_to=Sertifikat, null=True, blank=True)
    PortofolioTugasSiswa = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarPortofolioTugasSiswa = models.ImageField(upload_to=PortofolioTugasSiswa, null=True, blank=True)
    PortofolioTugasMateriPengembangan = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarPortofolioTugasMateriPengembangan = models.ImageField(upload_to=PortofolioTugasMateriPengembangan, null=True, blank=True)
    LaporanPrestasiSiswaLomba = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanPrestasiSiswaLomba = models.ImageField(upload_to=LaporanPrestasiSiswaLomba, null=True, blank=True)
    DataNilaiUjian = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDataNilaiUjian = models.ImageField(upload_to=DataNilaiUjian, null=True, blank=True)
    LaporanHasilTracerStudy = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanHasilTracerStudy = models.ImageField(upload_to=LaporanHasilTracerStudy, null=True, blank=True)
    #LaporanKegiatanProgramKreatif = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    #GambarLaporanKegiatanProgramKreatif = models.ImageField(upload_to=LaporanKegiatanProgramKreatif, null=True, blank=True)
    #LaporanKegiatanProgramKreatif = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    #GambarLaporanKegiatanProgramKreatif = models.ImageField(upload_to=LaporanKegiatanProgramKreatif, null=True, blank=True) 
    GambarKomponenMutuLulusan = models.ImageField(upload_to=KomponenMutuLulusan, null=True, blank=True)
    KomponenMutuLulusan = models.IntegerField(max_length=100)
    
    #Komponen Proses Pebelajaran
    LembarKerjaSiswa = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLembarKerjaSiswa = models.ImageField(upload_to=LembarKerjaSiswa, null=True, blank=True)
    KisiKisiSoalInstrumenHasilPenilaian = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarKisiKisiSoalInstrumenHasilPenilaian = models.ImageField(upload_to=KisiKisiSoalInstrumenHasilPenilaian, null=True, blank=True)
    AnalisisPencapaianKompetensi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarAnalisisPencapaianKompetensi = models.ImageField(upload_to=AnalisisPencapaianKompetensi, null=True, blank=True)
    JadwalRemedial = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarJadwalRemedial = models.ImageField(upload_to=JadwalRemedial, null=True, blank=True)
    RKS4Tahun = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarRKS4Tahun = models.ImageField(upload_to=RKS4Tahun, null=True, blank=True)
    RKAS1Tahun = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarRKAS1Tahun = models.ImageField(upload_to=RKAS1Tahun, null=True, blank=True)
    DaftarPenggunaanSapras = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDaftarPenggunaanSapras = models.ImageField(upload_to=DaftarPenggunaanSapras, null=True, blank=True)
    RPP = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarRPP = models.ImageField(upload_to=RPP, null=True, blank=True)
    #TataTertib = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    #GambarTataTertib = models.ImageField(upload_to=TataTertib, null=True, blank=True)
    GambarKomponenProsesPembelajaran = models.ImageField(upload_to=KomponenProsesPembelajaran, null=True, blank=True)
    KomponenProsesPembelajaran = models.IntegerField(max_length=100)
    
    #Komponen mutu guru
    RPP = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarRPP = models.ImageField(upload_to=RPP, null=True, blank=True)
    LaporanEvaluasi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanEvaluasi = models.ImageField(upload_to=LaporanEvaluasi, null=True, blank=True)
    LaporanDariSiswa = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanDariSiswa = models.ImageField(upload_to=LaporanDariSiswa, null=True, blank=True)
    LaporanDariGuru = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanDariGuru = models.ImageField(upload_to=LaporanDariGuru, null=True, blank=True)
    BuktiDaftarHadir = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarBuktiDaftarHadir = models.ImageField(upload_to=BuktiDaftarHadir, null=True, blank=True)
    LaporanPengembanganGuru = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanPengembanganGuru = models.ImageField(upload_to=LaporanPengembanganGuru, null=True, blank=True)
    LaporanKegiatanDiseminasi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanKegiatanDiseminasi = models.ImageField(upload_to=LaporanKegiatanDiseminasi, null=True, blank=True)
    #RPP = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    #GambarRPP = models.ImageField(upload_to=RPP, null=True, blank=True)
    GambarKomponenMutuGuru = models.ImageField(upload_to=KomponenMutuGuru, null=True, blank=True)
    KomponenMutuGuru = models.IntegerField(max_length=100)
    
    #Komponen Manajemen Sekolah
    DaftarHadirRapatVisiMisi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDaftarHadirRapatVisiMisi = models.ImageField(upload_to=DaftarHadirRapatVisiMisi, null=True, blank=True)
    LaporanKegiatanImplementasiVisiMisi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanKegiatanImplementasiVisiMisi = models.ImageField(upload_to=LaporanKegiatanImplementasiVisiMisi, null=True, blank=True)
    DokumenHasilEvaluasi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenHasilEvaluasi = models.ImageField(upload_to=DokumenHasilEvaluasi, null=True, blank=True)
    DokumenRekomendasi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenRekomendasi = models.ImageField(upload_to=DokumenRekomendasi, null=True, blank=True)
    DokumenVisiMisiSebelumnyaDanSetelah = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenVisiMisiSebelumnyaDanSetelah = models.ImageField(upload_to=DokumenVisiMisiSebelumnyaDanSetelah, null=True, blank=True)
    JadwalSupervisi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarJadwalSupervisi = models.ImageField(upload_to=JadwalSupervisi, null=True, blank=True)
    DokumenHasilObservasiKepsek = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenHasilObservasiKepsek = models.ImageField(upload_to=DokumenHasilObservasiKepsek, null=True, blank=True)
    DaftarHadirRapatRKSRKASdanNotulen = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDaftarHadirRapatRKSRKASdanNotulen = models.ImageField(upload_to=DaftarHadirRapatRKSRKASdanNotulen, null=True, blank=True)
    LaporanKegiatanPelaksanaanProgram = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanKegiatanPelaksanaanProgram = models.ImageField(upload_to=LaporanKegiatanPelaksanaanProgram, null=True, blank=True)
    DokumenKerjaSama = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenKerjaSama = models.ImageField(upload_to=DokumenKerjaSama, null=True, blank=True)
    DokumenPelaksanaanKegiatanKebersihan = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenPelaksanaanKegiatanKebersihan = models.ImageField(upload_to=DokumenPelaksanaanKegiatanKebersihan, null=True, blank=True)
    DokumenRKAS1Tahun = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenRKAS1Tahun = models.ImageField(upload_to=DokumenRKAS1Tahun, null=True, blank=True)
    DokumenRKAS4Tahun = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenRKAS4Tahun = models.ImageField(upload_to=DokumenRKAS4Tahun, null=True, blank=True)
    DaftarHadirRapatRKSRKASdanNotulen = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDaftarHadirRapatRKSRKASdanNotulen = models.ImageField(upload_to=DaftarHadirRapatRKSRKASdanNotulen, null=True, blank=True)
    RPP = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarRPP = models.ImageField(upload_to=RPP, null=True, blank=True)
    NotulenRakerKurikulum = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarNotulenRakerKurikulum = models.ImageField(upload_to=NotulenRakerKurikulum, null=True, blank=True)
    DokumenRakerEvaluasiKurikulum = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenRakerEvaluasiKurikulum = models.ImageField(upload_to=DokumenRakerEvaluasiKurikulum, null=True, blank=True)
    SOPPelaksanaanTugasGuru = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarSOPPelaksanaanTugasGuru = models.ImageField(upload_to=SOPPelaksanaanTugasGuru, null=True, blank=True)
    JadwalMengajarGuru = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarJadwalMengajarGuru = models.ImageField(upload_to=JadwalMengajarGuru, null=True, blank=True)
    DokumenPenilaianKriteriaGuru = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenPenilaianKriteriaGuru = models.ImageField(upload_to=DokumenPenilaianKriteriaGuru, null=True, blank=True)
    HasilPenilaianKinerjaGuru = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarHasilPenilaianKinerjaGuru = models.ImageField(upload_to=HasilPenilaianKinerjaGuru, null=True, blank=True)
    DokumenPenilaianKinerjaTendik = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenPenilaianKinerjaTendik = models.ImageField(upload_to=DokumenPenilaianKinerjaTendik, null=True, blank=True)
    HasilPenilaianKinerjaTendik = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarHasilPenilaianKinerjaTendik = models.ImageField(upload_to=HasilPenilaianKinerjaTendik, null=True, blank=True)
    BuktiSaksiAtauPenghargaan = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarBuktiSaksiAtauPenghargaan = models.ImageField(upload_to=BuktiSaksiAtauPenghargaan, null=True, blank=True)
    SOPPengelolaanSapras = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarSOPPengelolaanSapras = models.ImageField(upload_to=SOPPengelolaanSapras, null=True, blank=True)
    DokumenRapatPenyususanRAPBS = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenRapatPenyususanRAPBS = models.ImageField(upload_to=DokumenRapatPenyususanRAPBS, null=True, blank=True)
    RAPBS = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarRAPBS = models.ImageField(upload_to=RAPBS, null=True, blank=True)
    LaporanKeuangan1TahunTerakhir = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarLaporanKeuangan1TahunTerakhir = models.ImageField(upload_to=LaporanKeuangan1TahunTerakhir, null=True, blank=True)
    HasilCatatanAuditInternelEksternal3TahunTerakhir = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarHasilCatatanAuditInternelEksternal3TahunTerakhir = models.ImageField(upload_to=HasilCatatanAuditInternelEksternal3TahunTerakhir, null=True, blank=True)
    DokumenProgramEkstrakulikuler = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenProgramEkstrakulikuler = models.ImageField(upload_to=DokumenProgramEkstrakulikuler, null=True, blank=True)
    SuratTugasPembinaDanTimLomba = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarSuratTugasPembinaDanTimLomba = models.ImageField(upload_to=SuratTugasPembinaDanTimLomba, null=True, blank=True)
    SertifikatPrestasi = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarSertifikatPrestasi = models.ImageField(upload_to=SertifikatPrestasi, null=True, blank=True)
    DokumenProgramLayananBK = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenProgramLayananBK = models.ImageField(upload_to=DokumenProgramLayananBK, null=True, blank=True)
    DokumenRKATahunSebelumnya = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenRKATahunSebelumnya = models.ImageField(upload_to=DokumenRKATahunSebelumnya, null=True, blank=True)
    DokumenEvaluasiDiriTahunSebelumnya = models.CharField(max_length=50, choices=KEBUTUHAN_CHOICES)
    GambarDokumenEvaluasiDiriTahunSebelumnya = models.ImageField(upload_to=DokumenEvaluasiDiriTahunSebelumnya, null=True, blank=True)
    GambarKomponenManajemenSekolah = models.ImageField(upload_to=KomponenManajemenSekolah, null=True, blank=True)
    KomponenManajemenSekolah = models.IntegerField(max_length=100)


class Nilai(models.Model):
    Nilaiid = models.BigAutoField(primary_key=True)
    NamaNilai = models.CharField(max_length=50)
    RangeNilai = models.CharField(max_length=250)
    Warna = models.CharField(max_length=50)


class PolygonModel(models.Model):
    PolygonId = models.BigAutoField(primary_key=True)
    SekolahId = models.ForeignKey(PengajuanSekolah, on_delete=models.CASCADE)
    geometry = models.PolygonField()

    def __str__(self):
        return str(self.id)

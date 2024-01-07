from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import models
from .forms import *
# masyarakat
def landing_page(request):
    return render(request, "landing page/index.html")

def map(request):
    return render(request, "landing page/maps.html")

def verify(request):
    return render(request, "landing page/verify.html")

def pelaporan(request):
    return render(request, "landing page/pelaporan.html")

def pengajuan(request):
    return render(request, "landing page/pengajuan.html")

def about(request):
    return render(request, "landing page/about.html")

def kontak(request):
    return render(request, "landing page/kontak.html")

def loginadmin(request):
    return render(request, "core/login.html")

# fitur login
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        nip = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=nip, password=password)

        if user is not None:
            # User terotentikasi, lakukan login
            login(request, user)
            messages.success(request, 'Anda berhasil login')
            return redirect('home')  # Redirect setelah login berhasil
        else:
            # Autentikasi pengguna gagal
            messages.error(request, 'Kamu salah Password dan Username.')
            return redirect('loginadmin')

    return render(request, 'core/login.html')


# logout
def logoutadmin(request):
    logout(request)
    request.session.flush()
    return redirect('loginadmin')

def create_PengajuanSekolah(request):
    if request.method == 'POST':
        pengajuan_sekolah_form = PengajuanSekolahForm(request.POST, request.FILES)

        if pengajuan_sekolah_form.is_valid():
            # Simpan objek PengajuanSekolah
            pengajuan_sekolah = pengajuan_sekolah_form.save(commit=False)
            pengajuan_sekolah.NamaSekolah=request.POST['NamaSekolah'],
            pengajuan_sekolah.NamaKepalaSekolah=request.POST['NamaKepalaSekolah'],
            pengajuan_sekolah.NamaPengawasSekolah=request.POST['NamaPengawasSekolah'],
            pengajuan_sekolah.AlamatSekolah=request.POST['AlamatSekolah'],
            pengajuan_sekolah.JumlahGuruPNS=request.POST['GuruPNS'],
            pengajuan_sekolah.JumlahGuruHonorer=request.POST['GuruNonPNS'],
            pengajuan_sekolah.JumlahStaf=request.POST['Staf'],
            pengajuan_sekolah.JumlahSiswaX=request.POST['SiswaX'],
            pengajuan_sekolah.JumlahSiswaXI=request.POST['SiswaXI'],
            pengajuan_sekolah.JumlahSiswaXII=request.POST['SiswaXII'],
            pengajuan_sekolah.JumlahRuangKelas=request.POST['RuangKelas'],
            pengajuan_sekolah.StatusAkreditasi=request.POST['Akreditasi']
            # Dapatkan objek Status dengan nilai 'DIAJUKAN'
            status = Status.objects.create(tipestatus='DIAJUKAN')
            status.save()

            # Menghubungkan objek PengajuanSekolah dengan objek status dan sekolah
            pengajuan_sekolah.statusPengajuanSekolah = status
            pengajuan_sekolah.save()

            messages.success(request, 'Berhasil diajukan')
            return redirect('createpengajuan')  # Ganti 'peta' dengan URL halaman peta

        else:
            errors = pengajuan_sekolah_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')

    else:
        pengajuan_sekolah_form = PengajuanSekolahForm()

    return render(request, 'admin_sekolah/PengajuanSekolah.html', {'pengajuan_sekolah_form': pengajuan_sekolah_form})


# admin sekolah
#def loginp(request):
#    return render(request, "admin_sekolah/login.html")

def home(request):
    return render(request, "admin_sekolah/home.html")

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, "admin_sekolah/dashboard.html")

def profile(request):
    return render(request, "admin_sekolah/profile.html")

def PengajuanSekolah(request):
    if request.method == 'POST':
        pengajuan_sekolah_form = PengajuanSekolahForm(request.POST, request.FILES)

        if pengajuan_sekolah_form.is_valid():
            # Simpan objek PengajuanSekolah
            pengajuan_sekolah = pengajuan_sekolah_form.save(commit=False)
            pengajuan_sekolah.NamaSekolah=request.POST['NamaSekolah'],
            pengajuan_sekolah.NamaKepalaSekolah=request.POST['NamaKepalaSekolah'],
            pengajuan_sekolah.NamaPengawasSekolah=request.POST['NamaPengawasSekolah'],
            pengajuan_sekolah.AlamatSekolah=request.POST['AlamatSekolah'],
            pengajuan_sekolah.JumlahGuruPNS=request.POST['GuruPNS'],
            pengajuan_sekolah.JumlahGuruHonorer=request.POST['GuruNonPNS'],
            pengajuan_sekolah.JumlahStaf=request.POST['Staf'],
            pengajuan_sekolah.JumlahSiswaX=request.POST['SiswaX'],
            pengajuan_sekolah.JumlahSiswaXI=request.POST['SiswaXI'],
            pengajuan_sekolah.JumlahSiswaXII=request.POST['SiswaXII'],
            pengajuan_sekolah.JumlahRuangKelas=request.POST['RuangKelas'],
            pengajuan_sekolah.StatusAkreditasi=request.POST['Akreditasi']
            # Dapatkan objek Status dengan nilai 'DIAJUKAN'
            status = Status.objects.create(tipestatus='DIAJUKAN')
            status.save()

            # Menghubungkan objek PengajuanSekolah dengan objek status dan sekolah
            pengajuan_sekolah.statusPengajuanSekolah = status
            pengajuan_sekolah.save()

            messages.success(request, 'Berhasil diajukan')
            return redirect('createpengajuan')  # Ganti 'peta' dengan URL halaman peta

        else:
            errors = pengajuan_sekolah_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')

    else:
        pengajuan_sekolah_form = PengajuanSekolahForm()

    return render(request, 'admin_sekolah/PengajuanSekolah.html', {'pengajuan_sekolah_form': pengajuan_sekolah_form})

#def penilaian(request):
#    return render(request, "admin_sekolah/penilaian.html")

def koordinat(request):
    return render(request, "admin_sekolah/koordinat.html")

def edit_data(request):
    return render(request, "admin_sekolah/edit_data.html")

#def edit_penilaian(request):
#    return render(request, "admin_sekolah/edit_penilaian.html")

def edit_koordinat(request):
    return render(request, "admin_sekolah/edit_koordinat.html")

def pengajuan_akreditai(request):
    return render(request, "admin_sekolah/pengajuan_akreditasi.html")

def panduan(request):
    return render(request, "admin_sekolah/panduan.html")

def nilai_akhir(request):
    return render(request, "admin_sekolah/nilai_akhir.html")

#pengajuan akreditasi

#8 SNP
#def standar_kompetensi(request):
 #   return render(request, "snp/standar_kompetensi.html")

#def standar_isi(request):
#    return render(request, "snp/standar_isi.html")

#def standar_proses(request):
#   return render(request, "snp/standar_proses.html")

#def standar_penilaian_pendidikan(request):
#    return render(request, "snp/standar_penilaian_pendidikan.html")

#def standar_tenaga_kependidikan(request):
#    return render(request, "snp/standar_tenaga_kependidikan.html")

#def standar_sarana_prasarana(request):
#    return render(request, "snp/standar_sarana_prasarana.html")

#def standar_pengelolaan(request):
#    return render(request, "snp/standar_pengelolaan.html")

#def standar_pembiayaan(request):
#    return render(request, "snp/standar_pembiayaan.html")

#IASP
def komponen_mutu_lulusan(request):
    return render(request, "IASP/komponen_mutu_lulusan.html")

def komponen_proses_pembelajaran(request):
    return render(request, "IASP/komponen_proses_pembelajaran.html")

def komponen_mutu_guru(request):
    return render(request, "IASP/komponen_mutu_guru.html")

def komponen_manajemen_sekolah(request):
    return render(request, "IASP/komponen_manajemen_sekolah.html")


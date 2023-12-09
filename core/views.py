from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

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

# fitur login nya ya sayang
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
            return redirect('dashboard')  # Redirect setelah login berhasil
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




def panduan_masyarakat(request):
    return render(request, "masyarakat/panduan_masyarakat.html")

# admin sekolah
def loginp(request):
    return render(request, "admin_sekolah/login.html")

def home(request):
    return render(request, "admin_sekolah/home.html")

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, "admin_sekolah/dashboard.html")

def profile(request):
    return render(request, "admin_sekolah/profile.html")

def tambah_data(request):
    return render(request, "admin_sekolah/tambah_data.html")

def penilaian(request):
    return render(request, "admin_sekolah/penilaian.html")

def koordinat(request):
    return render(request, "admin_sekolah/koordinat.html")

def edit_data(request):
    return render(request, "admin_sekolah/edit_data.html")

def edit_penilaian(request):
    return render(request, "admin_sekolah/edit_penilaian.html")

def edit_koordinat(request):
    return render(request, "admin_sekolah/edit_koordinat.html")

def panduan(request):
    return render(request, "admin_sekolah/panduan.html")
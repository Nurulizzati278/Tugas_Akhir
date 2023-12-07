from django.shortcuts import render, redirect


# masyarakat
def landing_page(request):
    return render(request, "masyarakat/landing_page.html")

def map(request):
    return render(request, "masyarakat/map.html")

def about(request):
    return render(request, "masyarakat/about.html")

def panduan_masyarakat(request):
    return render(request, "masyarakat/panduan_masyarakat.html")

# admin sekolah
def login(request):
    return render(request, "admin_sekolah/login.html")

def home(request):
    return render(request, "admin_sekolah/home.html")

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
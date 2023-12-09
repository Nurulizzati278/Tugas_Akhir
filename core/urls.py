from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("map/", views.map, name="map"),
    path("about/", views.about, name="about"),
    path("verify/", views.verify, name="verify"),
    path("pelaporan/", views.pelaporan, name="pelaporan"),
    path("pengajuan/", views.pengajuan, name="pengajuan"),
    path("kontak/", views.kontak, name="kontak"),
    path("loginadmin/", views.loginadmin, name="loginadmin"),
    path("logoutadmin/", views.logoutadmin, name="logoutadmin"),
    path("user_login/", views.user_login, name="user_login"),
    
    
    # jangan ganggu yang baru
    path("panduan_masyarakat/", views.panduan_masyarakat, name="panduan_masyarakat"),
    path("loginp/", views.loginp, name="loginp"),
    # batassuci
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("tambah_data/", views.tambah_data, name="tambah_data"),
    path("penilaian/", views.penilaian, name="penilaian"),
    path("koordinat/", views.koordinat, name="koordinat"),
    path("edit_data/", views.edit_data, name="edit_data"),
    path("edit_penilaian/", views.edit_penilaian, name="edit_penilaian"),
    path("edit_koordinat/", views.edit_koordinat, name="edit_koordinat"),
    path("panduan/", views.panduan, name="panduan"),
]

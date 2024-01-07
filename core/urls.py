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
    # batassuci
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("PengajuanSekolah/", views.PengajuanSekolah, name="PengajuanSekolah"),
    path("koordinat/", views.koordinat, name="koordinat"),
    path("edit_data/", views.edit_data, name="edit_data"),
    path("edit_koordinat/", views.edit_koordinat, name="edit_koordinat"),
    path("pengajuan_akreditasi/", views.pengajuan_akreditai, name="pengajuan_akreditasi"),
    path("panduan/", views.panduan, name="panduan"),
    path("createpengajuan/",views.create_PengajuanSekolah, name="createpengajuan")
    
    #path("edit_penilaian/", views.edit_penilaian, name="edit_penilaian"),
    #path("penilaian/", views.penilaian, name="penilaian"),
    #path("nilai_akhir/", views.nilai_akhir, name="nilai_akhir"),
    
    #path("standar_kompetensi/", views.standar_kompetensi, name="standar_kompetensi"),
    #path("standar_isi/", views.standar_isi, name="standar_isi"),
    #path("standar_prose/", views.standar_proses, name="standar_proses"),
    #path("standar_penilaian_pendidikan/", views.standar_penilaian_pendidikan, name="standar_penilaian_pendidikan"),
    #path("standar_tenaga_kependidikan/", views.standar_tenaga_kependidikan, name="standar_tenaga_kependidikan"),
    #path("standar_sarana_prasarana/", views.standar_sarana_prasarana, name="standar_sarana_prasarana"),
    #path("standar_pengelolaan/", views.standar_pengelolaan, name="standar_pengelolaan"),
    #path("standar_pembiayaan/", views.standar_pembiayaan, name="standar_pembiayaan"),
    
    #path("komponen_mutu_lulusan/", views.komponen_mutu_lulusan, name="komponen_mutu_lulusan"),
    #path("komponen_proses_pembelajaran/", views.komponen_proses_pembelajaran, name="komponen_proses_pembelajaran"),
    #path("komponen_mutu_guru/", views.komponen_mutu_guru, name="komponen_mutu_guru"),
    #path("komponen_manajemen_sekolah/", views.komponen_manajemen_sekolah, name="komponen_manajemen_sekolah"),
]

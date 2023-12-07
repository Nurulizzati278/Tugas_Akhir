from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.landing_page,name='landing_page'),
    path('map/',views.map,name='map'),
    path('about/',views.about,name='about'),
    path('panduan_masyarakat/',views.panduan_masyarakat,name='panduan_masyarakat'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('tambah_data/',views.tambah_data,name='tambah_data'),
    path('penilaian/',views.penilaian,name='penilaian'),
    path('koordinat/',views.koordinat,name='koordinat'),
    path('edit_data/',views.edit_data,name='edit_data'),
    path('edit_penilaian/',views.edit_penilaian,name='edit_penilaian'),
    path('edit_koordinat/',views.edit_koordinat,name='edit_koordinat'),
    path('panduan/',views.panduan,name='panduan'),
    
]

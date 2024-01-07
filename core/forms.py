from django import forms
from .models import *


class PengajuanSekolahForm(forms.ModelForm):
    class Meta:
        model = PengajuanSekolah
        fields = "__all__"

    # AKREDITASI_CHOICES = (
    #     ("A", "SANGAT BAIK"),
    #     ("B", "BAIK"),
    #     ("C", "CUKUP"),
    #     ("TT", "TIDAK TERAKREDITASI"),
    # )
    # SekolahId = ()
    # NamaSekolah = forms.CharField(max_length=250)
    # NamaKepalaSekolah = forms.CharField(max_length=250)
    # NamaPengawasSekolah = forms.CharField(max_length=250)
    # AlamatSekolah = forms.CharField(max_length=500)
    # JumlahGuruPNS = forms.IntegerField(null=True, blank=True)
    # JumlahGuruHonorer = forms.IntegerField(null=True, blank=True)
    # JumlahStaf = forms.IntegerField(null=True, blank=True)
    # JumlahSiswaX = forms.IntegerField(null=True, blank=True)
    # JumlahSiswaXI = forms.IntegerField(null=True, blank=True)
    # JumlahSiswaXII = forms.IntegerField(null=True, blank=True)
    # JumlahRuangKelas = forms.IntegerField(null=True, blank=True)
    # StatusAkreditasi = models.CharField(max_length=50, choices=AKREDITASI_CHOICES)

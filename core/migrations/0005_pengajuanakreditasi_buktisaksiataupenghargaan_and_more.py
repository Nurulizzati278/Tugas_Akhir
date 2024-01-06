# Generated by Django 5.0 on 2024-01-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pengajuanakreditasi_analisispencapaiankompetensi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='BuktiSaksiAtauPenghargaan',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DaftarHadirRapatRKSRKASdanNotulen',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DaftarHadirRapatVisiMisi',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenEvaluasiDiriTahunSebelumnya',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenHasilEvaluasi',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenHasilObservasiKepsek',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenKerjaSama',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenPelaksanaanKegiatanKebersihan',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenPenilaianKinerjaTendik',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenPenilaianKriteriaGuru',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenProgramEkstrakulikuler',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenProgramLayananBK',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenRKAS1Tahun',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenRKAS4Tahun',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenRKATahunSebelumnya',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenRakerEvaluasiKurikulum',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenRapatPenyususanRAPBS',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenRekomendasi',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='DokumenVisiMisiSebelumnyaDanSetelah',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarBuktiSaksiAtauPenghargaan',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDaftarHadirRapatRKSRKASdanNotulen',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDaftarHadirRapatVisiMisi',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenEvaluasiDiriTahunSebelumnya',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenHasilEvaluasi',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenHasilObservasiKepsek',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenKerjaSama',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenPelaksanaanKegiatanKebersihan',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenPenilaianKinerjaTendik',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenPenilaianKriteriaGuru',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenProgramEkstrakulikuler',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenProgramLayananBK',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenRKAS1Tahun',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenRKAS4Tahun',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenRKATahunSebelumnya',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenRakerEvaluasiKurikulum',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenRapatPenyususanRAPBS',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenRekomendasi',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarDokumenVisiMisiSebelumnyaDanSetelah',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarHasilCatatanAuditInternelEksternal3TahunTerakhir',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarHasilPenilaianKinerjaGuru',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarHasilPenilaianKinerjaTendik',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarJadwalMengajarGuru',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarJadwalSupervisi',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarLaporanKegiatanImplementasiVisiMisi',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarLaporanKegiatanPelaksanaanProgram',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarLaporanKeuangan1TahunTerakhir',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarNotulenRakerKurikulum',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarRAPBS',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarSOPPelaksanaanTugasGuru',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarSOPPengelolaanSapras',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarSertifikatPrestasi',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='GambarSuratTugasPembinaDanTimLomba',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], max_length=50)),
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='HasilCatatanAuditInternelEksternal3TahunTerakhir',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='HasilPenilaianKinerjaGuru',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='HasilPenilaianKinerjaTendik',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='JadwalMengajarGuru',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='JadwalSupervisi',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='LaporanKegiatanImplementasiVisiMisi',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='LaporanKegiatanPelaksanaanProgram',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='LaporanKeuangan1TahunTerakhir',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='NotulenRakerKurikulum',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='RAPBS',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='SOPPelaksanaanTugasGuru',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='SOPPengelolaanSapras',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='SertifikatPrestasi',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanakreditasi',
            name='SuratTugasPembinaDanTimLomba',
            field=models.CharField(choices=[('ADA', 'ADA'), ('tIDAK ADA', 'TIDAK ADA')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
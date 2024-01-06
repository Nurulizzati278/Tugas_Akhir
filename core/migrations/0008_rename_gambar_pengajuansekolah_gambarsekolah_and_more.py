# Generated by Django 5.0 on 2024-01-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_akreditasiid_pengajuanakreditasi_akreditasiid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pengajuansekolah',
            old_name='Gambar',
            new_name='GambarSekolah',
        ),
        migrations.RenameField(
            model_name='pengajuansekolah',
            old_name='JumlahGuru',
            new_name='JumlahGuruHonorer',
        ),
        migrations.RenameField(
            model_name='pengajuansekolah',
            old_name='JumlahPegawai',
            new_name='JumlahGuruPNS',
        ),
        migrations.RenameField(
            model_name='pengajuansekolah',
            old_name='JumlahSiswa',
            new_name='JumlahSiswaX',
        ),
        migrations.RemoveField(
            model_name='pengajuansekolah',
            name='TahunBerdiri',
        ),
        migrations.AddField(
            model_name='pengajuansekolah',
            name='JumlahSiswaXI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuansekolah',
            name='JumlahSiswaXII',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuansekolah',
            name='JumlahStaf',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
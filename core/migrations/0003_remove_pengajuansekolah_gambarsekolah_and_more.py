# Generated by Django 5.0 on 2024-01-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_nilai_pengajuansekolah_alter_customuser_umur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengajuansekolah',
            name='GambarSekolah',
        ),
        migrations.AlterField(
            model_name='pengajuansekolah',
            name='AlamatSekolah',
            field=models.CharField(max_length=600),
        ),
    ]

# Generated by Django 4.2.2 on 2023-09-13 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rekapitulasi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rekap',
            old_name='absen',
            new_name='absen_id',
        ),
        migrations.RenameField(
            model_name='rekap',
            old_name='perizinan',
            new_name='perizinan_id',
        ),
        migrations.RenameField(
            model_name='rekap',
            old_name='presensi',
            new_name='presensi_id',
        ),
    ]
# Generated by Django 4.2.2 on 2023-09-12 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presensi', '0008_alter_presensi_tgl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presensi',
            name='tgl',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
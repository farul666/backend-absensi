# Generated by Django 4.2.2 on 2023-09-11 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presensi', '0004_alter_presensi_status_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presensi',
            name='tgl',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
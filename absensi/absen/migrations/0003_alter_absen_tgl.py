# Generated by Django 4.2.2 on 2023-09-12 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0002_alter_absen_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='tgl',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
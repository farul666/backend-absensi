# Generated by Django 4.2.2 on 2023-09-12 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0007_alter_perizinan_tgl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perizinan',
            name='tgl',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

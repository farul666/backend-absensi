# Generated by Django 4.2.2 on 2023-08-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0006_alter_perizinan_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perizinan',
            name='tgl',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0001_initial'),
        ('perizinan', '0004_alter_perizinan_tgl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perizinan',
            name='nama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biodata.biodata'),
        ),
    ]
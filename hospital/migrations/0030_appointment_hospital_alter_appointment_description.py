# Generated by Django 5.0.1 on 2024-04-20 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0029_remove_worker_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.admin'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.CharField(choices=[('BCG', 'BCG'), ('OPV(0)', 'OPV(0)'), ('Hep B', 'Hep B'), ('OPV1', 'OPV1'), ('Penta1(DPT+HepB+HiB)', 'Penta1(DPT+HepB+HiB)'), ('OPV2', 'OPV2'), ('Penta2(DPT+HepB+HiB)', 'Penta2(DPT+HepB+HiB)'), ('OPV3', 'OPV3'), ('Penta3(DPT+HepB+HiB)', 'Penta3(DPT+HepB+HiB)'), ('IPV', 'IPV'), ('MMR-1', 'MMR-1'), ('/MR/Measels', '/MR/Measels'), ('JE Vaccine-1', 'JE Vaccine-1'), ('OPV Booster', 'OPV Booster'), ('DPT 1st Booster', 'DPT 1st Booster'), ('JE Vaccine-2', 'JE Vaccine-2'), ('DPT 2nd Booster', 'DPT 2nd Booster'), ('TT1', 'TT1'), ('TT2', 'TT2')], max_length=100),
        ),
    ]
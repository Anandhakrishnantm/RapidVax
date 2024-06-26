# Generated by Django 5.0.1 on 2024-04-18 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0026_alter_admin_address_alter_admin_age_alter_admin_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.CharField(choices=[('ABC', 'ABC'), ('MNO', 'MNO')], max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(default='address', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='city',
            field=models.CharField(default='city', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='country',
            field=models.CharField(default='country', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Emergency Medicine Specialist', 'Emergency Medicine Specialist'), ('Allergist/Immunologist', 'Allergist/Immunologist'), ('Anesthesiologist', 'Anesthesiologist'), ('Colon and Rectal Surgeon', 'Colon and Rectal Surgeon')], default='Cardiologist', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='lastname',
            field=models.CharField(default='lastname', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='postalcode',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='address', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(default='city', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='country',
            field=models.CharField(default='country', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastname',
            field=models.CharField(default='lastname', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='postalcode',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

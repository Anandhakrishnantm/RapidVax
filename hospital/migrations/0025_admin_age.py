# Generated by Django 5.0.1 on 2024-01-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0024_covidvaccination"),
    ]

    operations = [
        migrations.AddField(
            model_name="admin",
            name="age",
            field=models.IntegerField(default=20),
        ),
    ]

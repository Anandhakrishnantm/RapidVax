# Generated by Django 3.1.5 on 2021-05-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_remove_admin_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

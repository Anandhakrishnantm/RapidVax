# Generated by Django 5.0.1 on 2024-04-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0028_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='name',
        ),
    ]

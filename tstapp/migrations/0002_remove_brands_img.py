# Generated by Django 5.1.1 on 2024-10-13 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='img',
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-27 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_auto_20200227_1631'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Upload',
            new_name='Upload_prescription',
        ),
        migrations.RenameModel(
            old_name='Upload_Prescriptions',
            new_name='Upload_reports',
        ),
    ]

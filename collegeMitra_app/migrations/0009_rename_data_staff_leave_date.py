# Generated by Django 4.1 on 2022-08-13 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeMitra_app', '0008_staff_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_leave',
            old_name='data',
            new_name='date',
        ),
    ]

# Generated by Django 4.1 on 2022-08-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeMitra_app', '0012_student_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_result',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]

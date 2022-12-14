# Generated by Django 4.1 on 2022-08-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeMitra_app', '0011_student_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_marks', models.IntegerField()),
                ('exam_marks', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeMitra_app.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeMitra_app.subject')),
            ],
        ),
    ]

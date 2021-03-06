# Generated by Django 4.0.4 on 2022-06-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsp', '0002_alter_student_faculty_alter_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default='Faculty', max_length=300),
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('SEMESTER', 'Semester'), ('FIRST', '1st Semester'), ('SECOND', '2nd Semester')], default='Semester', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='session',
            field=models.CharField(choices=[('SESSION', 'Session'), ('21/22', '2021/2022'), ('22/23', '2022/2023'), ('23/24', '2023/2024'), ('24/25', '2024/2025')], default='Session', max_length=50),
        ),
    ]

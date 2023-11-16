# Generated by Django 4.2.7 on 2023-11-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_course_session_year_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="admin",
        ),
        migrations.AddField(
            model_name="student",
            name="first_name",
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name="student",
            name="last_name",
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name="student",
            name="b_cnic",
            field=models.CharField(max_length=13),
        ),
    ]

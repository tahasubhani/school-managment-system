# Generated by Django 4.2.7 on 2023-11-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_student_student_regis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_regis",
            field=models.IntegerField(null=True),
        ),
    ]
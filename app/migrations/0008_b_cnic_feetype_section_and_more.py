# Generated by Django 4.2.7 on 2023-11-23 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_student_student_regis"),
    ]

    operations = [
        migrations.CreateModel(
            name="b_cnic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("b_cnic", models.CharField(max_length=100, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("address", models.CharField(max_length=200)),
                ("guardian_name", models.CharField(max_length=100)),
                ("guardian_phone", models.CharField(max_length=15)),
            ],
            options={
                "verbose_name_plural": "b_cnic",
            },
        ),
        migrations.CreateModel(
            name="FeeType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name="student",
            old_name="section_abc",
            new_name="section_id",
        ),
        migrations.AlterField(
            model_name="student",
            name="student_regis",
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100, null=True)),
                ("gender", models.CharField(max_length=100)),
                ("teacher_cnic", models.CharField(max_length=13, unique=True)),
                ("address", models.TextField(default="", max_length=255)),
                (
                    "salary",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "teacher_pic",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="media/teacher_pic"
                    ),
                ),
                ("joining_date", models.DateField(default="")),
                ("qualification", models.CharField(max_length=100)),
                (
                    "cv_resume",
                    models.FileField(
                        blank=True, default="", null=True, upload_to="media/teacher_cv"
                    ),
                ),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeePayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100, null=True)),
                ("date_of_payment", models.DateField()),
                ("fee_type", models.CharField(max_length=100)),
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "b_cnic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.b_cnic",
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
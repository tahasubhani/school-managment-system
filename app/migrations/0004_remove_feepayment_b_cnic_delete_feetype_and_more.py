# Generated by Django 4.2.7 on 2023-11-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_b_cnic_options_alter_student_student_regis"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feepayment",
            name="b_cnic",
        ),
        migrations.DeleteModel(
            name="FeeType",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="admin",
        ),
        migrations.AlterField(
            model_name="student",
            name="student_regis",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="b_cnic",
        ),
        migrations.DeleteModel(
            name="FeePayment",
        ),
        migrations.DeleteModel(
            name="Teacher",
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-23 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_alter_student_section_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="section",
            old_name="name",
            new_name="section_name",
        ),
    ]

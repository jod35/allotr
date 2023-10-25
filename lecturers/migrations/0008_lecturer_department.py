# Generated by Django 4.2.6 on 2023-10-25 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("departments", "0002_department_code"),
        ("lecturers", "0007_rename_course_lecturercourse_courses"),
    ]

    operations = [
        migrations.AddField(
            model_name="lecturer",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="departments.department",
            ),
            preserve_default=False,
        ),
    ]

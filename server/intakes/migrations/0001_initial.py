# Generated by Django 3.2.13 on 2023-08-22 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Intake",
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
                ("name", models.CharField(max_length=50)),
                ("start_date", models.DateTimeField(null=True)),
                ("end_date", models.DateField(null=True)),
                ("academic_year", models.IntegerField(default=2023)),
                (
                    "term",
                    models.CharField(
                        choices=[
                            ("Jan", "January"),
                            ("May", "May"),
                            ("Sep", "September"),
                        ],
                        default="Jan",
                        max_length=25,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="IntakeCourse",
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
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
                (
                    "intake",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="intakes.intake"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="intake",
            name="courses",
            field=models.ManyToManyField(
                through="intakes.IntakeCourse", to="courses.Course"
            ),
        ),
    ]

# Generated by Django 3.2.13 on 2023-08-22 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Program",
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
                ("name", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=10)),
                ("years_of_study", models.IntegerField(default=3)),
                (
                    "degree_level",
                    models.CharField(
                        choices=[
                            ("D", "Diploma"),
                            ("B", "Bachelors"),
                            ("PGd", "PostGraduateDiploma"),
                            ("M", "Masters"),
                        ],
                        max_length=50,
                    ),
                ),
                ("details", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "courses",
                    models.ManyToManyField(
                        related_name="programs", to="courses.Course"
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="departments.department",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]

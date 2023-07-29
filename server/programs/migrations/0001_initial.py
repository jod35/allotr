# Generated by Django 4.2.3 on 2023-07-29 08:58

from django.db import migrations, models
import django.db.models.deletion


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
                ("courses", models.ManyToManyField(to="courses.course")),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="departments.department",
                    ),
                ),
            ],
        ),
    ]

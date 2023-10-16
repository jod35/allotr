# Generated by Django 3.2.13 on 2023-08-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("code", models.CharField(max_length=10, unique=True)),
                ("title", models.CharField(max_length=225)),
                ("course_description", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
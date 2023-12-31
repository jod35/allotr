# Generated by Django 4.2.6 on 2023-11-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("code", models.CharField(max_length=5, unique=True)),
                ("dean", models.CharField(max_length=250)),
                ("contact_email", models.EmailField(max_length=80)),
                ("details", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
            ],
        ),
    ]

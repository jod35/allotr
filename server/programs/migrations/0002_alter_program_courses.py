# Generated by Django 4.2.3 on 2023-07-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
        ("programs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="courses",
            field=models.ManyToManyField(null=True, to="courses.course"),
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-11 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0002_programstructure"),
    ]

    operations = [
        migrations.AddField(
            model_name="programstructure",
            name="enrollment",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="programs.enrollment",
            ),
            preserve_default=False,
        ),
    ]

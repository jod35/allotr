# Generated by Django 3.2 on 2023-07-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='code',
            field=models.CharField(default=1, max_length=5, unique=True),
            preserve_default=False,
        ),
    ]

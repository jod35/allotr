# Generated by Django 3.2.13 on 2023-09-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
        ('lecturers', '0004_auto_20230822_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturercourse',
            name='courses',
        ),
        migrations.AddField(
            model_name='lecturercourse',
            name='program',
            field=models.ManyToManyField(related_name='lecturer', to='programs.Program'),
        ),
    ]

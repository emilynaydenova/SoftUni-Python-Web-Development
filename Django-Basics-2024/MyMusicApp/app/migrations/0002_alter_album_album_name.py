# Generated by Django 5.0.2 on 2024-02-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="album_name",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="Album Name"
            ),
        ),
    ]

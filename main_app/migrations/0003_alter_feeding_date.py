# Generated by Django 5.1.4 on 2025-01-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_feeding"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feeding",
            name="date",
            field=models.DateField(verbose_name="Feeding Date"),
        ),
    ]

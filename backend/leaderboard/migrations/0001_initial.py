# Generated by Django 5.2 on 2025-05-06 17:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserStats",
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
                ("total_hours_given", models.FloatField(default=0)),
                ("total_hours_received", models.FloatField(default=0)),
                ("sessions_completed", models.IntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

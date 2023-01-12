# Generated by Django 4.1.5 on 2023-01-12 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Favourites",
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
                ("ticker", models.CharField(max_length=8)),
                ("isfav", models.BooleanField()),
                (
                    "favslist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.user"
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-03 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empleado",
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
                ("nombre", models.CharField(max_length=150)),
                ("apellido", models.CharField(max_length=150)),
                ("salario", models.DecimalField(decimal_places=2, max_digits=8)),
                ("create_Ac", models.DateTimeField(auto_now=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

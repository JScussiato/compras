# Generated by Django 4.2.7 on 2023-12-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lcompras",
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
                ("nome", models.CharField(max_length=30)),
                ("unidade", models.CharField(blank=True, max_length=3, null=True)),
                ("codsetor", models.IntegerField(blank=True, null=True)),
                ("setor", models.CharField(blank=True, max_length=15, null=True)),
                ("preco", models.FloatField()),
                ("foto", models.ImageField(blank=True, upload_to="fotos/")),
            ],
        ),
    ]

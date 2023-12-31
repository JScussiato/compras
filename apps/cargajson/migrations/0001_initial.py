# Generated by Django 4.2.7 on 2023-12-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CargajsonImg",
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
                ("unidade", models.CharField(max_length=3)),
                ("setor", models.IntegerField()),
                ("preco", models.FloatField()),
                ("foto", models.ImageField(blank=True, upload_to="fotos/")),
            ],
        ),
    ]

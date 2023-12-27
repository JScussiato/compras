# Generated by Django 4.2.7 on 2023-12-25 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lcompras", "0006_remove_lcompras_codsetor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Setor",
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
            ],
        ),
        migrations.AlterField(
            model_name="lcompras",
            name="setor",
            field=models.IntegerField(
                choices=[
                    (1, "Açougue"),
                    (2, "Bebidas"),
                    (3, "Bomboniere"),
                    (4, "Conservas"),
                    (5, "Grãos"),
                    (6, "Limpeza"),
                    (7, "Hortifruti"),
                    (8, "Lacticínios"),
                    (9, "Organizadores"),
                    (10, "Padaria"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="lcompras",
            name="codsetor",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="lcompras.setor",
            ),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lcompras", "0017_alter_lcompras_setor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lcompras",
            name="setor",
            field=models.CharField(
                choices=[
                    ("Conservas", "Conservas"),
                    ("Graos", "Grãos"),
                    ("Bomboniere", "Bomboniére"),
                    ("Acougue", "Açougue"),
                    ("Limpeza", "Limpeza"),
                    ("Organizadores", "Organizadores"),
                    ("Hortifruti", "Hortifruti"),
                    ("Padaria", "Padaria"),
                    ("Laticinios", "Laticínios"),
                    ("Bebidas", "Bebidas"),
                ],
                default="",
                max_length=15,
            ),
        ),
    ]
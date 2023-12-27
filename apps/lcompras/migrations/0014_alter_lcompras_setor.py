# Generated by Django 4.2.7 on 2023-12-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lcompras", "0013_alter_lcompras_codsetor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lcompras",
            name="setor",
            field=models.IntegerField(
                choices=[
                    ("Conservas", "Conservas"),
                    ("Graos", "Graos"),
                    ("Bomboniere", "Bomboniere"),
                    ("Acougue", "Acougue"),
                    ("Limpeza", "Limpeza"),
                    ("Organizadores", "Organizadores"),
                    ("Hortifruti", "Hortifruti"),
                    ("Padaria", "Padaria"),
                    ("Laticinios", "Laticinios"),
                    ("Bebidas", "Bebidas"),
                ],
                default=1,
            ),
        ),
    ]

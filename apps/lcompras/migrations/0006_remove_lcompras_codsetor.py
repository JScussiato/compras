# Generated by Django 4.2.7 on 2023-12-25 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lcompras", "0005_lcompras_codsetor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lcompras",
            name="codsetor",
        ),
    ]

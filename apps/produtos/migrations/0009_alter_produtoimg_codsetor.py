# Generated by Django 4.2.7 on 2023-12-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0008_alter_produtoimg_unidade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtoimg",
            name="codsetor",
            field=models.CharField(default="", editable=False, max_length=2),
        ),
    ]

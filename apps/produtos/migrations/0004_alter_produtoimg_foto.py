# Generated by Django 4.2.7 on 2023-12-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0003_alter_produtoimg_setor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtoimg",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/"),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0004_alter_produtoimg_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtoimg",
            name="setor",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

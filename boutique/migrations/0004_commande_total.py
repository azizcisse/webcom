# Generated by Django 4.2.3 on 2023-07-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boutique", "0003_rename_code_commande_zipcode"),
    ]

    operations = [
        migrations.AddField(
            model_name="commande",
            name="total",
            field=models.CharField(default="500000", max_length=200),
            preserve_default=False,
        ),
    ]
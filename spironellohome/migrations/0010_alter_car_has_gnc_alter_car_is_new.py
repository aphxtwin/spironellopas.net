# Generated by Django 4.1.5 on 2023-02-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0009_rename_quote_visitordata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="has_gnc",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="car",
            name="is_new",
            field=models.BooleanField(),
        ),
    ]

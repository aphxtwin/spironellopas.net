# Generated by Django 4.1.5 on 2023-02-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0029_alter_car_has_gnc_alter_car_is_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="has_gnc",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="car",
            name="is_new",
            field=models.BooleanField(default=False),
        ),
    ]

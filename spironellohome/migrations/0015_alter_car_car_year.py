# Generated by Django 4.1.5 on 2023-02-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0014_alter_car_car_brand_alter_car_car_model_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_year",
            field=models.IntegerField(),
        ),
    ]
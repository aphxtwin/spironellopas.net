# Generated by Django 4.1.5 on 2023-02-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0015_alter_car_car_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_version",
            field=models.CharField(max_length=150),
        ),
    ]
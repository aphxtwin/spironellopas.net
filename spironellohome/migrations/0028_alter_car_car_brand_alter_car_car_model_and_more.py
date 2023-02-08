# Generated by Django 4.1.5 on 2023-02-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0027_alter_car_has_gnc_alter_car_is_new_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_brand",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_model",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="insurancelist",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="visitordata",
            name="email",
            field=models.EmailField(max_length=255),
        ),
    ]
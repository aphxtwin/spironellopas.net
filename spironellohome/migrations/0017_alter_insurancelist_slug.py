# Generated by Django 4.1.5 on 2023-02-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0016_alter_car_car_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insurancelist",
            name="slug",
            field=models.SlugField(blank=True, max_length=355, null=True),
        ),
    ]
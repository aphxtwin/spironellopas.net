# Generated by Django 4.1.5 on 2023-02-03 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0018_remove_insurancelist_product_abreviation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visitordata",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="visitordata",
            name="phone_prefix",
        ),
    ]
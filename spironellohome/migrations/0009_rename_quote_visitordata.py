# Generated by Django 4.1.5 on 2023-02-03 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0008_alter_insurancelist_product_abreviation"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Quote",
            new_name="VisitorData",
        ),
    ]
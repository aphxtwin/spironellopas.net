# Generated by Django 4.1.5 on 2023-02-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spironellohome", "0032_learningarticles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="learningarticles",
            name="summary",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
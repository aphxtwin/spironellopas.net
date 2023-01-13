# Generated by Django 4.0.5 on 2023-01-11 15:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketPlaceProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_field', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=300)),
                ('product_explanation', ckeditor.fields.RichTextField()),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2023-01-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spironellohome', '0002_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceproducts',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]

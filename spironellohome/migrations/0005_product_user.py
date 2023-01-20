# Generated by Django 4.0.5 on 2023-01-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spironellohome', '0004_marketplaceproducts_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('products', models.ManyToManyField(to='spironellohome.product')),
            ],
        ),
    ]

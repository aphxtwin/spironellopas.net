# Generated by Django 4.0.5 on 2023-01-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spironellohome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.CharField(max_length=10000)),
            ],
        ),
    ]
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    products = models.ManyToManyField(Product)

class MarketPlaceProducts(models.Model):
    title = models.CharField(max_length=100)
    image_field = models.ImageField()
    description = models.CharField(max_length=300)
    icon = models.ImageField(null=True, blank=True)
    product_explanation = RichTextField()
    slug = models.SlugField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Footer(models.Model):
    about_text = models.CharField(max_length=10000)

    
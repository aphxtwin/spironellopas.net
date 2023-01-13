from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class MarketPlaceProducts(models.Model):
    title = models.CharField(max_length=100)
    image_field = models.ImageField()
    description = models.CharField(max_length=300)
    product_explanation = RichTextField()
    
    def __str__(self):
        return self.title
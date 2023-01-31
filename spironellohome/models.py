from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class InsuranceList(models.Model):
    '''
    This model is used for the list of insurance products of the company
    '''
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

class Quote(models.Model):
    '''
    This model is used for the home page quick quote form 
    '''
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone_prefix = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    products = models.ManyToManyField(InsuranceList)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} {self.surname}"

class Car(models.Model):
    '''
    This model is used for the home page quick quote form 
    '''
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.CharField(max_length=4)
    car_version = models.CharField(max_length=100)
    has_gnc = models.BooleanField()
    is_it_new = models.BooleanField()
    fast_quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    def __str__(self):
        return self.car_brand

class Footer(models.Model):
    about_text = models.CharField(max_length=10000)

    
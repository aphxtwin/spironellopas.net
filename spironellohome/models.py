from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class InsuranceList(models.Model):
    '''
    This model is used for the list of insurance products of the company
    '''
    title = models.CharField(max_length=100)
    image_field = models.ImageField()
    description = models.CharField(max_length=3000)
    icon = models.ImageField(null=True, blank=True)
    product_explanation = RichTextField()
    slug = models.SlugField(max_length=255, blank=True, null=True)
    product_abreviation = models.CharField(max_length=20, default="other")
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class LearningArticles(models.Model):
    '''
    This model is used for the learning articles
    '''
    title = models.CharField(max_length=250, null=False, blank=False) 
    summary = models.CharField(max_length=1000, blank = True)
    image = models.ImageField(null=True, blank =True) 
    image_description = models.CharField(max_length = 255, blank = True)
    date_posted = models.DateTimeField(auto_now_add = True)
    body = RichTextField(default = '')
    slug = models.SlugField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Section(models.Model):
    '''
    This model is used for the div elements with title-heading and paragraphs of the 
    learning articles.
    '''
    title = models.CharField(max_length=100, null=False, blank=False)
    body = RichTextField(default = '')
    article = models.ForeignKey(LearningArticles, on_delete=models.CASCADE, related_name='sections')
    def __str__(self):
        return self.title
    
class VisitorData(models.Model):
    '''
    This model is used for storing personal data of the visitor 
    that wants to get a quote 
    '''
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} {self.surname}"

class Car(models.Model):
    '''
    This model is used to store the car information
    '''
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_version = models.CharField(max_length=150)
    has_gnc = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.car_brand} {self.car_model} {self.car_year}"

class House(models.Model):
    '''
    This model is used to store the house information
    '''
    metros_cuadrados_cubiertos = models.CharField(max_length=100)
    tipo_de_vivienda = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.tipo_de_vivienda}"
        

class Footer(models.Model):
    about_text = models.CharField(max_length=800)

    
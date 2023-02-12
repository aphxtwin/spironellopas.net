from django import forms
from django.forms import inlineformset_factory
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.InsuranceList)
admin.site.register(models.VisitorData)
admin.site.register(models.Footer)
admin.site.register(models.House)
admin.site.register(models.Car)

class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = '__all__'

class SectionInline(admin.StackedInline):
    model = models.Section
    extra = 1
    form = SectionForm
class LearningArticlesAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

admin.site.register(models.LearningArticles, LearningArticlesAdmin)
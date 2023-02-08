from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.InsuranceList)
admin.site.register(models.VisitorData)
admin.site.register(models.Footer)
admin.site.register(models.House)
admin.site.register(models.Car)



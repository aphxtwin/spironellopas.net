from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("marketplace", views.marketplace, name="marketplace"),
    path("marketplace/<slug:slug>", views.product_detail, name= 'product_detail')
]

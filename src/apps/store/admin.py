from django.contrib import admin
from .models import ProductModel, ProductDetail
admin.register(ProductModel, site=True)
admin.register(ProductDetail, site=True)

from django.contrib import admin
from .models import ProductModel, Category

admin.site.register(ProductModel)
admin.site.register(Category)
# admin.site.register(ProductDetail)


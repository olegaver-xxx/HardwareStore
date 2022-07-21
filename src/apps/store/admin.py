from django.contrib import admin
from .models import ProductModel, Category, Price, ProductImageModel


class ImagesInline(admin.StackedInline):
    model = ProductImageModel
    fields = 'file',
    extra = 0


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)


admin.site.register(Price)
admin.site.register(Category)
# admin.site.register(ProductDetail)

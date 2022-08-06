from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import ProductModel, Category, Price, ProductImageModel


class ImagesInline(admin.StackedInline):
    model = ProductImageModel
    fields = 'file',
    extra = 0


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'codename')
    list_per_page = 500

admin.site.register(Price)
admin.site.register(Category)
# admin.site.register(ProductDetail)

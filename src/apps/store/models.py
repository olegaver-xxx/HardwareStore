from pathlib import Path

from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    category_icon = models.ImageField(upload_to="category", blank=True, null=True)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    # banner = models.ImageField(upload_to='products/', blank=True, null=True)
    product_name = models.CharField(max_length=32)
    about = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # price = models.CharField(max_length=16)
    def __str__(self):
        return self.product_name

    @property
    def previews(self):
        return self.images.all()


def upload_image(instance, filename):
    path = Path('products', str(instance.product.pk), filename)
    return path.as_posix()


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return f"{self.product} Image"


class Price(models.Model):
    sum = models.DecimalField(decimal_places=2, max_digits=10)
    product = models.OneToOneField('store.ProductModel', on_delete=models.CASCADE, related_name='price')

    def __str__(self):
        return str(self.sum)

# class ProductDetail(models.Model):
#     banner = models.ImageField(upload_to="category")
#     name = models.CharField(max_length=64)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

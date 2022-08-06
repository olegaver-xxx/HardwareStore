from django import forms
from .models import ProductModel, ProductImageModel
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput)

    class Meta:
        model = ProductModel
        fields = '__all__'

class ProductImageForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=ProductModel.objects.all(),
                                    widget=forms.HiddenInput)
    class Meta:
        model = ProductImageModel
        fields = '__all__'


# class AddCategoryForm:
#     class Meta:
#         from .models import Category
#         model = Category
#         fields = '__all__'

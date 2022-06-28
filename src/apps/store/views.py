from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import ProductModel

class IndexView(TemplateView):
    template_name = 'store/index.html'

class ProductModelView(ListView):
    template_name = 'store/product_list.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 16




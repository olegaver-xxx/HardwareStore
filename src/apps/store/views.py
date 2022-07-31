from django.views.generic import TemplateView, ListView, DetailView
# from django.http import HttpResponse
from functools import reduce
import operator

from django.db.models import Q
from .models import ProductModel


# class IndexView(TemplateView):
#     template_name = 'store/index.html'


# class ProductModelView(ListView):
#     template_name = 'store/product_list.html'
#     model = ProductModel
#     context_object_name = 'products'
#     paginate_by = 16
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         query = self.request.GET.get('q')
#         if query:
#             search_list = [x.strip() for x in query.split() if x.strip()]
#             if query:
#                 qs = qs.filter(
#                     reduce(operator.or_, [Q(product_name__icontains=q) | Q(about__icontains=q) for q in search_list])
#                 )
#         return qs
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         ctx = super(ProductModelView, self).get_context_data()
#         query = self.request.GET.get('q')
#         if query:
#             ctx['query'] = query.strip()
#         return ctx


class ProductDetailView(DetailView):
    template_name = 'store/product_detail.html'
    model = ProductModel
    context_object_name = 'product_detail'



class IndexView(ListView):
    # template_name = 'store/product_list.html'
    template_name = 'store/products.html'
    model = ProductModel
    context_object_name = 'product_list'
    paginate_by = 10
    ordering = 'pk',


# class TestBaseView(TemplateView):
#     template_name = 'product_detail.html'
#     model = ProductModel
#     context_object_name = 'test_base'

# class SearchView(ListView):
#     model = ProductModel
#     template_name = 'store/search.html'
#     context_object_name = 'search'

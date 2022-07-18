from django.views.generic import TemplateView, ListView, DetailView
# from django.http import HttpResponse
from django.db.models import Q
from .models import ProductModel, ProductDetail


class IndexView(TemplateView):
    template_name = 'store/index.html'


class ProductModelView(ListView):
    template_name = 'store/product_list.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 16

class ProductDetailView(DetailView):
    template_name = 'store/product_detail.html'
    model = ProductDetail
    context_object_name = 'product_details'

# class SearchView(ListView):
#     model = ProductModel
#     template_name = 'store/search.html'
#     context_object_name = 'search'
class SearchResultsView(ListView):
    model = ProductModel
    template_name = 'store/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = ProductModel.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import formset_factory
from django import forms
from django.db.models import Q
# from django.http import HttpResponse
from functools import reduce
import operator

from django.db.models import Q
from .models import ProductModel
from .forms import ProductForm, ProductImageForm


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

    def get_queryset(self):  # new
        query: str = self.request.GET.get("q", '')
        search_list: list = [x.strip() for x in query.split() if x.strip()]
        qs = super().get_queryset()
        if search_list:
            query_filter = reduce(operator.or_, (Q(product_name__icontains=item,) for item in search_list))
            qs = qs.filter(query_filter)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get("q") or ''
        return ctx

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            success_url = "/"
            return redirect(reverse('products'))

    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})
# class TestBaseView(TemplateView):
#     template_name = 'product_detail.html'
#     model = ProductModel
#     context_object_name = 'test_base'

class SearchResultsView(ListView):
    model = ProductModel
    template_name = 'store/search.html'
    context_object_name = 'objects'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     ctx = super(SearchResultsView, self).get_context_data(object_list=None, **kwargs)
    #     ctx['q'] = self.request.GET['q']
    #     return ctx

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = ProductModel.objects.filter(
            Q(product_name=query) | Q(about=query)
        )
        return object_list

class ProductCreateView(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    permission_required = ['store.add_productmodel', 'store.change_productmodel']
    success_url = '/'
    template_name = 'store/create.html'
    context_object_name = 'prodcreate'
    ImageFormSet = formset_factory(ProductImageForm, extra=5)
    # formset = ImageFormSet(request.POST, request.FILES)
    # if request.method == 'POST':
    #     formset = ImageFormSet(request.POST, request.FILES)
    #     if formset.is_valid():
    #         pass
    # else:
    #     formset = ImageFormSet()
    # print(formset)
    # for f in formset:
    #     print(f.as_table())
    def get(self, request):
        print('ffffff')
        return super(ProductCreateView, self).get(request)
    # forms
    # def get_initial(self):
    #     return dict(
    #         author=self.request.user
    #     )


# def create_multiple(request):
#     print('asdasd')
#     ImageFormSet = formset_factory(ProductImageForm, extra=5)
#     if request.method == 'POST':
#         formset = ImageFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             pass
#     else:
#         formset = ImageFormSet()
#     print(formset)
#     for f in formset:
#         print(f.as_table())
#     return render(request, 'store/create.html', {'formset': formset})




# class AddCategoryView(CreateView, PermissionRequiredMixin):
#     form_class = AddCategoryForm
#     model = Category
#     permission_required = 'store.add_category'
#     success_url = '/'
#     context_object_name = 'addcat'
#     template_name = 'store/addcat.html'
#     def get_initial(self):
#         return dict(
#             author=self.request.user
#         )
# @login_required
# def create_multiple_photos(request):
#     PhotoFormSet = formset_factory(forms.PhotoForm, extra=5)
#     formset = PhotoFormSet()
#     if request.method == 'POST':
#         pass
#     return render(request, 'store/create.html', {'formset': formset})
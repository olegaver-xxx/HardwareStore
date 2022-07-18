from django.contrib import admin
from django.urls import path
from apps.store.views import ProductModelView, ProductDetailView, SearchResultsView

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', ProductModelView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('search', SearchResultsView.as_view(), name='search_results')
}
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.store.views import IndexView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    # path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from apps.store.views import IndexView, ProductDetailView, signup, SearchResultsView, ProductCreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html', success_url='/'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('addproduct/', ProductCreateView.as_view(), name='add'),
    # path('addproduct/', create_multiple, name='add'),
    # path('accounts/profile/', ..., name='profile'),
    # path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('addcat/', AddCategoryView.as_view(), name='addcat'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = TemplateView.as_view(template_name='error.html')

from django.contrib import admin
from django.urls import path
from apps.store.views import IndexView, ProductModelView

urlpatterns = {
    path('', ProductModelView.as_view(), name='products'),
    path('admin/', admin.site.urls),
}

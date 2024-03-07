from django.urls import path
from .views import disease_classification, index, product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path('disease-predict', disease_classification, name='predict_with_model'),
    path('product-list', product_list, name='product_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

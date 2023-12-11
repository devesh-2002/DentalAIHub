# appname/urls.py
from django.urls import path
from .views import disease_classification, index, product_list, upload_form
from .views import symptom_checker_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('symptom-checker/', symptom_checker_view, name='symptom_checker'),
    path('predict/', disease_classification, name='predict_with_model'),
    path('upload/', upload_form, name='upload_form'),
    path('products/', product_list, name='product_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

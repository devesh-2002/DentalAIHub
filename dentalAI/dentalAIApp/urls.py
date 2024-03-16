from django.urls import path
from .views import disease_classification, index, ner_view, product_list, query_openai_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path('disease-predict', disease_classification, name='predict_with_model'),
    path('product-list', product_list, name='product_list'),
    path('chatbot',query_openai_view, name='query_openai_view'),
    path('ner-prescription',ner_view, name='ner_view')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

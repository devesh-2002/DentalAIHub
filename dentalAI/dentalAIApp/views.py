from imp import load_module
import os
from django.http import JsonResponse
from django.shortcuts import render
import numpy as np
from PIL import Image 
from .models import MedicalProduct
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from django.views.decorators.csrf import csrf_exempt


from django_nextjs.render import render_nextjs_page_sync
def index(request):
    return render_nextjs_page_sync(request)
@csrf_exempt 
def disease_classification(request):
    if request.method == 'POST':
        model_path = '../model/dental_classification.h5'
        model = load_model(model_path)

        try:
            uploaded_image = request.FILES['image']
            image = Image.open(uploaded_image)
            image = image.resize((150, 150))
            image_array = np.array(image) / 255.0 
            input_data = np.expand_dims(image_array, axis=0)
        except Exception as e:
            return JsonResponse({'error': str(e)})

        predictions = model.predict(input_data)
        max_prediction = float(np.max(predictions)) 

        predicted_class = np.argmax(predictions)

        image_path = os.path.join('media', 'uploaded_images', uploaded_image.name)
        with open(image_path, 'wb') as img_file:
            for chunk in uploaded_image.chunks():
                img_file.write(chunk)

        return JsonResponse({
            'image_path': image_path,
            'predictions': max_prediction,
            'predicted_disease': get_disease_label(predicted_class)
        }, encoder=DjangoJSONEncoder)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})

def get_disease_label(predicted_class):
    disease_labels = ['Caries', 'Gingivitis', 'Tooth Discoloration', 'Mouth Ulcer', 'Hypodontia', 'Calculus']

    if 0 <= predicted_class < len(disease_labels):
        return disease_labels[predicted_class]
    else:
        return 'Unknown'

@csrf_exempt 
def product_list(request):
    products = MedicalProduct.objects.all()
    serialized_products = [
        {'name': product.name, 'image': product.image, 'price':product.price}  
        for product in products
    ]
    return JsonResponse(serialized_products, safe=False)
# views.py
from imp import load_module
from django.shortcuts import render

from dentalAIapp.models import Product
from .symptom_checker import SymptomCheckerBot
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  
import tensorflow as tf
from PIL import Image
import numpy as np
import os
from tensorflow import keras
from keras.models import load_model
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    return HttpResponse('Hello')
import pickle

def load_model_from_file(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
dataset = [
    {
        "symptom": "Toothache",
        "questions": [
            {"question": "Is the pain constant or intermittent?", "label": None},
            {"question": "Do you feel sensitivity to hot or cold?", "label": None},
            {"question": "Is the pain triggered by biting or chewing?", "label": None},
            {"question": "Have you noticed any swelling or redness in the affected area?", "label": None},
            {"question": "Do you notice any bad taste in your mouth?", "label": None},
            {"question": "Do you have difficulty in opening your mouth?", "label": None},
            {"question": "Have you experienced any recent injury to your mouth?", "label": None},
            {"question": "Is there any visible cavity or hole in your tooth?", "label": None},
            {"question": "Do you grind your teeth at night?", "label": None},
            {"question": "Have you been diagnosed with any systemic conditions like diabetes?", "label": None},
            {"question": "Have you taken any over-the-counter pain relievers, and did they help?", "label": None},
            {"question": None, "label": "Caries"}
        ]
    },
    {
        "symptom": "Bleeding Gums",
        "questions": [
            {"question": "Do your gums bleed when you brush or floss?", "label": None},
            {"question": "Have you noticed any swelling or redness in your gums?", "label": None},
            {"question": "Do you wear braces or any dental appliances?", "label": None},
            {"question": "Have you ever had a tooth pulled out?", "label": None},
            {"question": "Have you experienced any recent injury to your mouth?", "label": None},
            {"question": "Do you take any blood-thinning medications?", "label": None},
            {"question": "Have you changed your toothbrush or oral hygiene routine recently?", "label": None},
            {"question": None, "label": "Gingivitis"}
        ]
    },
    {
        "symptom": "Tooth Sensitivity",
        "questions": [
            {"question": "Do you feel a sharp pain when consuming hot or cold beverages?", "label": None},
            {"question": "Does the sensitivity linger after the stimulus is removed?", "label": None},
            {"question": "Do you have any visible cracks or fractures in your teeth?", "label": None},
            {"question": "Do you use a hard-bristle toothbrush?", "label": None},
            {"question": "Have you noticed any receding gums?", "label": None},
            {"question": "Have you had any recent dental procedures?", "label": None},
            {"question": "Have you changed your toothpaste recently?", "label": None},
            {"question": None, "label": "Tooth Sensitivity"}
        ]
    },
    {
        "symptom": "Mouth Ulcer",
        "questions": [
            {"question": "Do you have a painful sore or lesion in your mouth?", "label": None},
            {"question": "Is the sore white or yellowish with a red border?", "label": None},
            {"question": "Have you had multiple ulcers at the same time?", "label": None},
            {"question": "Do you have a history of mouth ulcers?", "label": None},
            {"question": "Have you been under increased stress recently?", "label": None},
            {"question": "Do you have any nutritional deficiencies?", "label": None},
            {"question": None, "label": "Mouth Ulcer"}
        ]
    },
    {
        "symptom": "Cracked Tooth",
        "questions": [
            {"question": "Have you experienced a sudden and sharp pain when biting or chewing?", "label": None},
            {"question": "Does the pain come and go?", "label": None},
            {"question": "Is there any visible crack or fracture in your tooth?", "label": None},
            {"question": "Do you have a habit of clenching or grinding your teeth?", "label": None},
            {"question": "Have you recently experienced trauma to your mouth?", "label": None},
            {"question": "Do you have a history of large fillings in your tooth?", "label": None},
            {"question": None, "label": "Cracked Tooth"}
        ]
    },
    {
        "symptom": "Cavities",
        "questions": [
            {"question": "Do you have visible holes or pits in your teeth?", "label": None},
            {"question": "Do you feel pain or sensitivity when consuming sweet, hot, or cold items?", "label": None},
            {"question": "Have you noticed any discoloration on your teeth?", "label": None},
            {"question": "Do you experience bad breath?", "label": None},
            {"question": "Is there a family history of dental cavities?", "label": None},
            {"question": "Do you consume sugary snacks or drinks frequently?", "label": None},
            {"question": None, "label": "Cavities"}
        ]
    },
    {
        "symptom": "Tooth Discoloration",
        "questions": [
            {"question": "Have you noticed any changes in the color of your teeth?", "label": None},
            {"question": "Is the discoloration localized to a specific tooth or generalized?", "label": None},
            {"question": "Have you recently consumed foods or drinks that may stain teeth?", "label": None},
            {"question": "Do you have a history of smoking or tobacco use?", "label": None},
            {"question": "Have you had any recent trauma to your mouth?", "label": None},
            {"question": None, "label": "Tooth Discoloration"}
        ]
    },
    {
        "symptom": "Hypodontia",
        "questions": [
            {"question": "Do you have fewer teeth than normal?", "label": None},
            {"question": "Have you noticed gaps or spaces between your teeth?", "label": None},
            {"question": "Is there a family history of missing teeth?", "label": None},
            {"question": "Have you undergone orthodontic treatment in the past?", "label": None},
            {"question": "Do you have any syndromes or medical conditions associated with tooth abnormalities?", "label": None},
            {"question": None, "label": "Hypodontia"}
        ]
    },
    {
        "symptom": "Oral Cancer",
        "questions": [
            {"question": "Have you noticed any unusual lumps or sores in your mouth?", "label": None},
            {"question": "Is there persistent hoarseness or difficulty in swallowing?", "label": None},
            {"question": "Do you have a history of tobacco or alcohol use?", "label": None},
            {"question": "Have you been exposed to human papillomavirus (HPV)?", "label": None},
            {"question": "Have you noticed any changes in your voice or speech patterns?", "label": None},
            {"question": "Is there unexplained weight loss?", "label": None},
            {"question": None, "label": "Oral Cancer"}
        ]
    },
    {
        "symptom": "Unknown",
        "questions": [
            {"question": "I'm sorry, I couldn't understand. Can you please provide more details about your symptoms?", "label": None},
            {"question": None, "label": "Unknown"}
        ]
    }
]
symptom_bot = SymptomCheckerBot(dataset)

@csrf_exempt
def symptom_checker_view(request):
    if request.method == "POST":
        user_response = request.POST.get('userResponse', '').lower()
        bot = SymptomCheckerBot(dataset)
        current_symptom_data = bot.get_current_symptom_data()

        if 'start' in request.POST and request.POST['start'] == 'true':
            context = {"questions": current_symptom_data["questions"]}
        else:
            bot.ask_question(current_symptom_data, user_response)
            bot_response = bot.get_bot_response()
            context = {"bot_response": bot_response, "user_responses": bot.user_responses}

        if bot.current_symptom >= len(bot.dataset):
            context["message"] = "Symptom checking completed!"

        return JsonResponse(context)

    else:
        bot = SymptomCheckerBot(dataset)
        current_symptom_data = bot.get_current_symptom_data()
        context = {"questions": current_symptom_data["questions"]}
        return JsonResponse(context)

@csrf_exempt
def disease_classification(request):
    if request.method == 'POST':
        model_path = 'models/dental_classification.h5'
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
        max_prediction = float(np.max(predictions))  # Convert to Python float

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

def upload_form(request):
    return render(request, 'upload_form.html')


def product_list(request):
    products = Product.objects.all()
    serialized_products = [
        {'name': product.name, 'image': product.image}  
        for product in products
    ]
    return JsonResponse(serialized_products, safe=False)


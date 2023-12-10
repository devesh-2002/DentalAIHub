import json
from django.http import JsonResponse
from transformers import BertTokenizer, BertForSequenceClassification
import torch

def get_medical_recommendations(predicted_label):
    recommendations = {
        "Caries": "Consider using fluoride toothpaste and consult a dentist for further evaluation.",
        "Gingivitis": "Maintain good oral hygiene, including regular brushing and flossing. Consult a dentist for professional cleaning.",
        "Tooth Sensitivity": "Use a toothpaste for sensitive teeth and avoid extreme temperatures. Consult a dentist for personalized advice.",
        "Mouth Ulcer": "Rinse your mouth with saltwater and avoid spicy foods. If persistent, consult a dentist.",
        "Cracked Tooth": "Avoid chewing on hard objects and consult a dentist for possible treatment options.",
        "Cavities": "Maintain good oral hygiene, limit sugary foods, and consult a dentist for cavity treatment.",
        "Tooth Discoloration": "Avoid smoking and limit foods that may stain teeth. Consult a dentist for teeth whitening options.",
        "Hypodontia": "Consult an orthodontist for evaluation and potential treatment options.",
        "Oral Cancer": "Seek immediate medical attention. Consult a healthcare professional for further evaluation.",
        "Unknown": "I'm sorry, I couldn't understand. Please consult a healthcare professional for personalized advice."
    }
    return recommendations.get(predicted_label, "No specific recommendation available.")

class SymptomCheckerBot:
    def __init__(self, dataset):
        with open("conversation.json", "r") as file:
            self.dataset = json.load(file)
        self.dataset = dataset
        self.current_symptom = 0
        self.user_responses = {}
        self.no_count = 0
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
        self.model.eval()  # Set the model to evaluation mode
        
    def load_dataset(self):
        with open("conversation.json", "r") as file:
            return json.load(file)

    def ask_question(self, symptom_data, user_response):
        for question_data in symptom_data["questions"]:
            question = question_data.get("question")
            label = question_data.get("label")

            # Use the user_response parameter instead of console input
            # user_response = input(f"{question} (yes/no): ").lower()
            self.user_responses[question] = user_response

            if user_response == 'yes':
                self.no_count = 0
            else:
                self.no_count += 1

                if self.no_count >= 2:
                    self.no_count = 0
                    self.change_symptom()
                    return

            if label:
                print("\nBased on your responses, you may have:", label)
                if label != "Unknown":
                    classification_result = self.perform_classification(label)
                    print("BERT Classification Result:", classification_result)
                    recommendation = get_medical_recommendations(label)
                    print("Medical Recommendation:", recommendation)

                    # Update the symptom index for the next iteration
                    self.current_symptom += 1

                if self.no_count >= 2:
                    self.no_count = 0
                    self.change_symptom()
                    return

            if label:
                print("\nBased on your responses, you may have:", label)
                if label != "Unknown":
                    classification_result = self.perform_classification(label)
                    print("BERT Classification Result:", classification_result)
                    recommendation = get_medical_recommendations(label)
                    print("Medical Recommendation:", recommendation)

                    # Update the symptom index for the next iteration
                    self.current_symptom += 1

    def change_symptom(self):
        # Logic to change the symptom for the next iteration
        self.current_symptom += 1
    
    def get_bot_response(self):
        # Logic to generate bot response based on user responses
        return "Bot response placeholder"

    def perform_classification(self, text):
        # Logic to perform BERT classification
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        return predicted_class
    
    def get_current_symptom_data(self):
        return self.dataset[self.current_symptom]

# Main block (for testing purposes)
if __name__ == "__main__":
    with open("conversation.json", "r") as file:
        dataset = json.load(file)

    bot = SymptomCheckerBot(dataset)
    bot.ask_question(dataset[bot.current_symptom])

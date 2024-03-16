from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import pytesseract
from PIL import Image

tokenizer = AutoTokenizer.from_pretrained("Clinical-AI-Apollo/Medical-NER")
model = AutoModelForTokenClassification.from_pretrained("Clinical-AI-Apollo/Medical-NER")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_entities_from_image(file):
    extracted_text = pytesseract.image_to_string(Image.open(file))
    tokens = tokenizer(extracted_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)
    predictions = torch.argmax(outputs.logits, dim=2)
    predicted_labels = [model.config.id2label[label_id] for label_id in predictions[0].tolist()]
    combined_results = list(zip(tokenizer.convert_ids_to_tokens(tokens["input_ids"][0]), predicted_labels))
    return combined_results

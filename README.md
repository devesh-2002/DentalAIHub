# DentalAIHub
## Welcome to DentalAIHub!
### About DentalAIHub
DentalAIHub is an AI based Dental E-Clinic, where you can identify your dental disease in just a matter of few seconds. This project contains several features : 
1. **AI ChatBot** : This chatbot interacts with users, and can identify the possibility of a disease by the user's symptoms. This is a RAG based OpenAI chatbot. 
2. **Disease Classification** : Just enter a photo of the affected part of your mouth, and get to know the possibility of a dental disease. This is a CNN Model, which is made by fine tuning a pretrained model - XCeption.
3. **Natural Entity Recognition** : Detect Entities from a Dental Prescription. Pytessaract used for Image to Text conversion and pre-trained model DBERT, fine tuned on Clinical NER used for detecting Entities.  
4. **Medical Store** : This is a Medical Store exclusively related to Oral health.


### Tech Stack
1. Django
2. Next.js
3. Shadcn/ui 
4. Jupyter Notebook
5. PostgreSQL

### Installation
1. Fork and Clone the Repository
   ```
   git clone https://github.com/<username>/DentalAIHub
   ```
3. Create a new env folder
   ```
   virtualenv env
   ```
   ```
   source env/Scripts/activate
   ```
5. Install the requirements.txt file
   ```
   pip install -r requirements.txt
    ```
6. In the dentalAI/frontend folder, type : 

    ```
   npm install
   ```
7. Run the backend and frontend separately :
 
In frontend folder : 
   ```
   npm run build
   npm start
   ```
   
In main folder : 
   ```
   export DJANGO_SETTINGS_MODULE="dentalAI.settings"
   django-admin manage.py runserver
   ```


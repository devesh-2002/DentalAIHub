# DentalAIHub
## Welcome to DentalAIHub!
### About DentalAIHub
DentalAIHub is an AI based Dental E-Clinic, where you can identify your dental disease in just a matter of few seconds. This project contains several features : 
1. **AI ChatBot** : This chatbot interacts with users, and can identify the possibility of a disease by the user's symptoms. Also, this bot gives suggestions to users based on symptoms. This bot is made by fine-tuning of pretrained BERT Model (bert-base-uncased).
2. **Disease Classification** : Just enter a photo of the affected part of your mouth, and get to know the possibility of a dental disease. This is a CNN Model, which is made by fine tuning a pretrained model - XCeption.
3. **Medical Store** : This is a Medical Store exclusively related to Oral health.


### Tech Stack
1. Django
2. Next.js
3. Shadcn/ui 
4. Jupyter Notebook
5. PostgreSQL
6. Stripe

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
   env/Scripts/activate
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
   django-admin manage.py runserver
   ```


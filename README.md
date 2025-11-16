# Email Spam Detector – Machine Learning Project

This is an Email Spam Detection system built using Python, Scikit-Learn, and Streamlit.  
The model uses TF-IDF Vectorization and Logistic Regression to classify messages as Spam or Ham (Not Spam).

FEATURES

• Classifies messages as Spam or Not Spam  
• Uses TF-IDF for text vectorization  
• Machine learning model: Logistic Regression  
• Interactive Streamlit Web App  
• Clean and simple project structure  

PROJECT STRUCTURE

Email-Spam-Detector/

├── app.py                       
├── mail_data.csv                
├── model.joblib 
├── vectorizer.joblib     
├── requirements.txt             
└── README.md                    

MODEL TRAINING DETAILS

• Dataset: mail_data.csv  
• Missing values replaced with empty strings  
• Category converted: ham = 0, spam = 1  
• Train-test split: 80% training / 20% testing  
• TF-IDF Vectorizer (stop_words='english', lowercase=True)  
• Classifier: Logistic Regression  
• Model and vectorizer saved using joblib  

TRAINING PROCESS

1. Load dataset with pandas  
2. Replace null values  
3. Convert labels (ham/spam → 0/1)  
4. Apply TF-IDF vectorizer  
5. Train Logistic Regression model  
6. Print training & testing accuracy  
7. Save model and vectorizer  

To train the model again:
python model.py


RUNNING THE STREAMLIT APP

Install dependencies:
pip install -r requirements.txt

Run the web app:
streamlit run app.py


USAGE

1. Open the Streamlit application  
2. Enter or paste any message  
3. Click "Classify"  
4. The app predicts:
   ✔ Ham (Not Spam)
   🚫 Spam


TECHNOLOGIES USED

• Python  
• Pandas  
• Scikit-Learn  
• TF-IDF Vectorizer  
• Logistic Regression  
• Streamlit  
• Joblib  

PURPOSE OF THIS PROJECT

This project helps understand:
• Text classification  
• Feature extraction using TF-IDF  
• Building ML models  
• Deployment using Streamlit  
• Organizing ML projects for GitHub  

CONTRIBUTION

You can fork this repository and improve the UI, accuracy, or model.


This project is open-source and available for learning.

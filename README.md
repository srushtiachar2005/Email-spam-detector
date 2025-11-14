Email Spam Detector - Project Documentation

This project is an Email Spam Detection system built using Python, Scikit-Learn, and Streamlit. The machine learning model uses TF-IDF Vectorization and Logistic Regression to classify messages as Spam or Ham (Not Spam).

Model Training Details:
The model is trained using the file mail_data.csv.
The dataset is cleaned by replacing missing values.
The Category column is converted:
ham = 0
spam = 1

Text messages (Message column) are used as input features.
The dataset is split into training and testing sets with an 80:20 ratio.

TF-IDF Vectorizer is used to convert text into numerical features.
Logistic Regression is used as the machine learning classifier.
The trained model and vectorizer are saved using joblib.

Project Structure:

model.py : Script to train and save the ML model

app.py : Streamlit web application

mail_data.csv : Dataset used for training

spam_classifier_model.joblib : Saved Logistic Regression model

tfidf_vectorizer.joblib : Saved TF-IDF vectorizer

requirements.txt : Project dependencies

README.txt : Project documentation

How Training Works:

Dataset is loaded using pandas.

Missing values are replaced with empty strings.

Category values are converted to numeric form.

Text messages are vectorized using TF-IDF (with stop_words='english').

Logistic Regression model is trained on the features.

Training and testing accuracy is printed.

The trained model and vectorizer are saved as .joblib files.

Installation Instructions:

Install Python 3.

Install required libraries:
pip install -r requirements.txt

To train the model again, run:
python model.py

To start the web app, run:
streamlit run app.py

Usage:
Enter a message in the Streamlit interface.
The app loads the trained model and TF-IDF vectorizer.
It predicts whether the message is Spam or Ham.

Technologies Used:

Python

Pandas

Scikit-Learn

Logistic Regression

TF-IDF Vectorizer

Streamlit

Joblib

Purpose:
This project helps in understanding text classification, vectorization, and machine learning model deployment using Streamlit.

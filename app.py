import streamlit as st
import joblib


model = joblib.load('model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

st.title("Email Spam Detector")
st.write("Write your Gmail text below:")


user_input = st.text_area("Enter the email text here")

if st.button("Classify Text"):
    if user_input.strip() == "":
        st.warning("Please enter some text before classifying.")
    else:
        input_features = vectorizer.transform([user_input])
        prediction = model.predict(input_features)

        st.write("---")
        st.write(" Result:")
        if prediction[0] == 1:
            st.error("🚫 This Email is SPAM!")
        else:
            st.success("✔ This Email is HAM (Not Spam)")

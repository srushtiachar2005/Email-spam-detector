import streamlit as st
import joblib
import imaplib
import email
from email.header import decode_header

model=joblib.load('spam_classifier_model.joblib')
vectorizer=joblib.load('tfidf_vectorizer.joblib')

st.title("Email Spam Detector")

st.write("Login to your Gmail")


gmail_user=st.text_input("Enter the Gmail Address")
gmail_password=st.text_input("Enter the Gmail Password",type="password")

if st.button("Login & Fetch Emails"):

    try:
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(gmail_user, gmail_password)
        mail.select("inbox")

        # If login is successful, we fetch emails:
        status, messages = mail.search(None, "ALL")

        if status != "OK":
            st.error("Failed to fetch emails from inbox.")
            st.stop()

        email_ids = messages[0].split()

        st.success("Login Successful! Select an email to classify.")

        # Get last 20 emails
        last_20 = email_ids[-20:]

        email_texts = []

        for num in reversed(last_20):
            status, msg_data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            email_texts.append((num, subject))

        email_choice = st.selectbox(
            "Choose an email to scan:",
            [f"{i+1}. {sub}" for i, (_, sub) in enumerate(email_texts)]
        )

        selected_idx = int(email_choice.split(".")[0]) - 1
        email_id, subject = email_texts[selected_idx]

        # Fetch full email body
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        body = ""
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body = part.get_payload(decode=True).decode()
                except:
                    pass

        st.write("### 📨 Email Body:")
        st.write(body)

        input_features = vectorizer.transform([body])
        prediction = model.predict(input_features)

        st.write("---")
        st.write("## 🔍 Result:")
        if prediction[0] == 1:
            st.error("🚫 This Email is SPAM!")
        else:
            st.success("✔ This Email is HAM (Not Spam)")

    except imaplib.IMAP4.error as e:
        st.error("Login Failed. Please check email or app password.")
        st.info("Use a Gmail App Password (NOT your normal Gmail password).")
        st.stop()

    except Exception as e:
        st.error("Unexpected error:")
        st.error(str(e))
        st.stop()

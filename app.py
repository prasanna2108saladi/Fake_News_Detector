import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load dataset (You can replace this with a larger one)
data = {
    'text': [
        "Donald Trump says COVID-19 is under control.",
        "NASA confirms the discovery of water on the moon.",
        "Aliens have landed in India.",
        "Apple releases the new iPhone with hologram feature.",
        "Government announces free education for all."
    ],
    'label': ["FAKE", "REAL", "FAKE", "FAKE", "REAL"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Load them back (simulate production use)
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Streamlit UI
st.set_page_config(page_title="📰 Fake News Detector", layout="centered")
st.title("📰 Real-Time Fake News Detector")

user_input = st.text_area("Enter news content to check if it's fake or real:")

if st.button("Check News"):
    if user_input.strip() != "":
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        if prediction == "REAL":
            st.success("✅ This news appears to be REAL.")
        else:
            st.error("🚫 Warning: This news appears to be FAKE.")
    else:
        st.warning("Please enter some news text to analyze.")

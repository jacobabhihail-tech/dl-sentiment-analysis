import joblib
import re

# Load model + vectorizer (ONLY ONCE)
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Clean function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Predict function
def predict_sentiment(text):
    clean = [clean_text(text)]
    vec = vectorizer.transform(clean)
    prediction = model.predict(vec)
    return prediction[0]

# Run script
if __name__ == "__main__":
    text = input("Enter a review: ")
    result = predict_sentiment(text)
    print("Sentiment:", result)
# Sentiment Analysis using Machine Learning

## 📌 Project Overview
This project is a simple Sentiment Analysis system that classifies text into:
- Positive
- Negative
- Neutral

It uses Natural Language Processing (NLP) and Machine Learning to analyze user reviews.

---

## 🚀 Problem Statement
Companies receive thousands of user reviews daily.  
Manually analyzing them is difficult.

This system automates sentiment detection from text data.

---

## 🧠 How It Works
Pipeline:

Text → Cleaning → Tokenization → Vectorization → Model → Prediction

- Text Cleaning: Removes noise (punctuation, symbols)
- Tokenization: Breaks text into words
- Vectorization: Converts text into numbers (CountVectorizer)
- Model: Multinomial Naive Bayes

---

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- Joblib

---

## 📂 Project Structure

dl-sentiment-analysis/
│
├── data/
├── models/
│ ├── sentiment_model.pkl
│ └── vectorizer.pkl
│
├── notebook/
│ └── sentiment_analysis.ipynb
│
├── src/
│ └── predict.py
│
├── README.md


---


## ▶️ How to Run

1. Clone the repo
2. Navigate to project folder
3. Run:

```bash
python src/predict.py
```
---

## Example

Input : This movie is amazing

Output : Sentiment : Positive

---



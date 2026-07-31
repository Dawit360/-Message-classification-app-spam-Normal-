# 📧 Spam Detection AI System

A machine learning-based web application that detects whether a message is **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) and multiple classification models.

---

## 🚀 Project Overview

This project builds a complete **Spam Detection Pipeline**, including:

- Data preprocessing
- Feature extraction (TF-IDF / Count Vectorizer)
- Model training & comparison
- Best model selection
- Flask web application for real-time prediction
- Deployment using Ngrok

---

## 🧠 Models Used

The following machine learning models were trained and evaluated:

- Logistic Regression
- Naive Bayes (MultinomialNB)
- Support Vector Machine (LinearSVC)
- Random Forest
- Gradient Boosting
- Decision Tree
- K-Nearest Neighbors
- Perceptron

---

## 🏆 Best Model

The best-performing model was selected based on **F1 Score**.

**TF-IDF + Linear SVM (LinearSVC)** typically performs best for text classification tasks.

---

## 📂 Project Structure

SMS-Spam-Classification/
│
├── app.py                  # Flask application
├── Model/
│   ├── spam_model.pkl      # Trained model
│   └── vectorizer.pkl      # Text vectorizer
│
├── templates/
│   └── index.html          # Frontend UI
│
├── results/
│   └── model_results.csv   # Model performance results
│
├── Dataset/                # Training datasets
│
└── README.md

---

## 🧑‍💻 User Installation Guide

Follow these steps to run the Spam Detection app locally or in Google Colab.

---

### 🔹 Option 1: Run Locally (Recommended)

#### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/SMS-Spam-Classification.git
cd SMS-Spam-Classification

#### 2. Install Dependencies

pip install flask scikit-learn pandas numpy

#### 3. Run the Flask App

python app.py

#### 4. Open in Browser

http://127.0.0.1:5000

---

### 🔹 Option 2: Run in Google Colab (with Public URL)

#### 1. Upload or Clone Project

#### 2. Install Dependencies

!pip install flask pyngrok scikit-learn pandas numpy

#### 3. Start Flask Server

!python app.py > log.txt 2>&1 &

#### 4. Generate Public URL

from pyngrok import ngrok
url = ngrok.connect(5000)
print(url)

#### 5. Open the App

Use the generated public URL to access the app.

---

## 🖥️ Web Interface

- Enter a message
- Click **Predict**
- Get result: **Spam / Not Spam**

---

## 📊 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score

F1 Score is used as the main metric for model selection.

---

## 💡 Features

- End-to-end ML pipeline
- Multiple model comparison
- Real-time prediction via Flask
- Simple and clean UI
- Easy deployment

---

## 🔐 Notes

- Do not upload large datasets to GitHub
- Keep API tokens (ngrok, etc.) private

---

## 👨‍💻 Author

**Dawit**

---

## ⭐ Acknowledgments

- Scikit-learn
- Flask
- Ngrok
- Open datasets for spam classification

---

## 📌 Future Improvements

- Deploy to cloud (Render / Railway / AWS)
- Add deep learning models (LSTM, BERT)
- Improve UI/UX
- Add email integration

---

⭐ If you like this project, give it a star!

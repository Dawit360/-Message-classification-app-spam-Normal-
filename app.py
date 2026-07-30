
from flask import Flask, render_template, request
import joblib
import os


app = Flask(__name__)


# =========================
# PATHS
# =========================

MODEL_PATH = "Model/spam_model.pkl"
VECTORIZER_PATH = "Model/vectorizer.pkl"


# =========================
# LOAD MODEL
# =========================

print("Loading model...")

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(VECTORIZER_PATH)

print("Model loaded successfully!")



# =========================
# HOME PAGE
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    message = ""


    if request.method == "POST":

        message = request.form["message"]


        # Convert text into features
        features = vectorizer.transform(
            [message]
        )


        # Predict
        result = model.predict(features)[0]


        if result == 1:
            prediction = "🚨 SPAM MESSAGE"

        else:
            prediction = "✅ NORMAL MESSAGE"



    return render_template(
        "index.html",
        prediction=prediction,
        message=message
    )



# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )

from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")  # Home
def home():
    return "Program is up and running"


@app.route("/predict", methods=["POST"])  # Predict
def predict():
    content = request.json
    try:
        data = [content["age"], content["bmi"], content["smoker"]]
        data = pd.DataFrame([data], columns=["age", "bmi", "smoker"])
        prediction = model.predict(data)
        response = {
            "code": 200,
            "message": "Prediction successful",
            "prediction": prediction[0],
        }
        return jsonify(response)
    except Exception as e:
        response = {"code": 500, "message": "Prediction failed", "error": str(e)}
        return jsonify(response)


app.run()

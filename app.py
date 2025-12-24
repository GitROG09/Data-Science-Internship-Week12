from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df_scaled = scaler.transform(df)
    prob = model.predict_proba(df_scaled)[:, 1]
    return jsonify({"churn_probability": float(prob[0])})

if __name__ == "__main__":
    app.run(debug=True)

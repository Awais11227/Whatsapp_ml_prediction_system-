import joblib
import numpy as np

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from preprocessing import parse_features

app = Flask(__name__)

# Load model + scaler + feature order
model = joblib.load("artifacts/model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")
feature_names = joblib.load("artifacts/features.pkl")

EXPECTED_FEATURES = len(feature_names)

CLASS_NAMES = {
    0: "No Churn",
    1: "Churn"
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():

    incoming_msg = request.values.get("Body", "").strip()

    print("Incoming:", incoming_msg)

    response = MessagingResponse()

    try:
        features = parse_features(incoming_msg, EXPECTED_FEATURES)

    except ValueError as e:
        response.message(
            f"❌ Input Error: {e}\n\n"
            f"Send {EXPECTED_FEATURES} numbers separated by commas."
        )
        return str(response)

    # Convert to numpy
    X = np.array(features).reshape(1, -1)

    # Scale
    X_scaled = scaler.transform(X)

    # Predict
    prediction = int(model.predict(X_scaled)[0])
    probability = model.predict_proba(X_scaled)[0]
    confidence = probability.max()

    label = CLASS_NAMES[prediction]

    final_response = (
        f"✅ Prediction: {label}\n"
        f"Confidence: {confidence:.2%}"
    )

    print(final_response)

    response.message(final_response)
    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
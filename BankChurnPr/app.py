from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import pandas as pd
import traceback
import sys

# Initialize Flask app
app = Flask(__name__)
# Enable CORS
CORS(app)

# Load the NEW 10-feature test model globally when the server starts
MODEL_PATH = r"C:\Users\ASUS\Desktop\test_model.pkl"
print(f"Loading model from {MODEL_PATH}...")
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("Test model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(".", path)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Manually extract the 10 features directly in exactly the format training expected
        feature_dict = {
            'CreditScore': [float(data.get('credit_score', 0))],
            'Geography': [str(data.get('geography', ''))],
            'Gender': [str(data.get('gender', ''))],
            'Age': [float(data.get('age', 0))],
            'Tenure': [float(data.get('tenure', 0))],
            'Balance': [float(data.get('balance', 0))],
            'NumOfProducts': [float(data.get('num_products', 0))],
            'HasCrCard': [int(data.get('has_crcard', 0))],
            'IsActiveMember': [int(data.get('is_active_member', 0))],
            'EstimatedSalary': [float(data.get('estimated_salary', 0))]
        }

        # The scikit-learn pipeline expects a pandas DataFrame with matching column names
        df = pd.DataFrame(feature_dict)

        # Attempt to get probability
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(df)
            churn_prob = float(probabilities[0][1])
        elif hasattr(model, "predict"):
            prediction = model.predict(df)
            churn_prob = float(prediction[0])
        else:
            return jsonify({"error": "Loaded object has no predict method"}), 500

        # Return the prediction response
        return jsonify({
            "churn_probability": churn_prob
        })

    except Exception as e:
        print("Error during prediction:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Start the local development server
    print("Starting ML Model Backend Server...")
    app.run(host="127.0.0.1", port=5000, debug=True)

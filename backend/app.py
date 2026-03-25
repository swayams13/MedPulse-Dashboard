from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os, json
import pandas as pd
from utils.predict import predict_burnout
from utils.email_sender import send_email

app = Flask(__name__)
CORS(app)

DATA_FILE = "data/records.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    os.makedirs("temp", exist_ok=True)
    filepath = os.path.join("temp", file.filename)
    file.save(filepath)

    result = predict_burnout(filepath)

    data = load_data()
    new_entry = {
        "id": len(data) + 1,
        "burnout": result["prediction"],
        "confidence": result["confidence"]
    }
    data.append(new_entry)
    save_data(data)

    return jsonify(result)

@app.route("/records", methods=["GET"])
def get_records():
    return jsonify(load_data())

@app.route("/download-excel", methods=["GET"])
def download_excel():
    data = load_data()
    df = pd.DataFrame(data)

    file_path = "data/burnout.xlsx"
    df.to_excel(file_path, index=False)

    return send_file(file_path, as_attachment=True)

@app.route("/send-email", methods=["POST"])
def email():
    data = load_data()
    send_email(data)
    return jsonify({"message": "Email sent successfully"})

if __name__ == "__main__":
    app.run(debug=True)

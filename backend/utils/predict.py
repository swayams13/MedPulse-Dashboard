import numpy as np
from utils.feature_extractor import extract_features

# ⚠️ Dummy logic if model not present
def predict_burnout(image_path):
    features = extract_features(image_path)
    score = np.mean(features)

    if score < 0.3:
        prediction = "Low"
    elif score < 0.6:
        prediction = "Medium"
    else:
        prediction = "High"

    return {
        "prediction": prediction,
        "confidence": float(np.random.uniform(70, 95)),
        "probabilities": {
            "Low": 30,
            "Medium": 40,
            "High": 30
        }
    }

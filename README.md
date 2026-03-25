# 🫀 MedPulse AI — Physician Burnout Intelligence System

## 📌 Overview

MedPulse AI is an intelligent healthcare analytics platform designed to **detect physician burnout early** using prescription handwriting analysis. The system leverages **computer vision + machine learning** to extract visual features from handwritten prescriptions and predict burnout levels.

This project addresses a critical healthcare challenge:

> Burnout in doctors often goes unnoticed until it affects performance, patient safety, and mental health.

---

## 🚀 Key Features

### 🏥 Hospital Admin Dashboard

* Real-time monitoring of all doctors
* Burnout categorization: **Low / Medium / High**
* Individual doctor insights and intervention suggestions
* Scalable dashboard for hospital-level analytics

### 👨‍⚕️ Doctor Personal View

* Personalized burnout analysis (baseline comparison)
* Burnout Drift Index (BDI)
* Probability breakdown for each burnout level
* Actionable recommendations

### 🔬 Live Burnout Detection

* Upload prescription images (PNG/JPG)
* No OCR dependency (works even on degraded handwriting)
* Extracts **12 visual handwriting features**
* Instant burnout prediction with confidence score

### 📊 Data Management & Reporting

* Persistent storage of all predictions
* Download reports in **CSV / Excel**
* Email report sharing functionality

---

## 🧠 Machine Learning Pipeline

### 🔹 Feature Extraction (Computer Vision)

The system extracts the following features directly from images:

* tremor_index
* stroke_variance
* edge_density
* num_blobs
* blur_metric
* ink_density
* horiz_profile_std
* vert_profile_std
* local_contrast
* blob_area_std
* avg_blob_area
* skewness

### 🔹 Model

* Trained using **Scikit-learn**
* Supports classification:

  * Low Burnout
  * Medium Burnout
  * High Burnout

### 🔹 Pipeline

```
Image → Feature Extraction → Scaling → Model Prediction → Result
```

---

## 🏗️ Project Architecture

```
medpulse-ai/
│
├── backend/
│   ├── app.py                # Flask API
│   ├── model/               # Trained ML model
│   ├── utils/               # Feature extraction & prediction logic
│   ├── data/                # Stored records
│   └── requirements.txt
│
├── frontend/
│   ├── index.html           # UI Dashboard
│   └── dashboard_data.json
│
└── README.md
```

---

## ⚙️ Tech Stack

### Frontend

* HTML5, CSS3, JavaScript
* Interactive dashboard UI

### Backend

* Python
* Flask (REST API)
* Flask-CORS

### Machine Learning

* Scikit-learn
* OpenCV
* NumPy / Pandas

### Data Handling

* JSON (local storage)
* Excel export (Pandas)

---

## 🔌 API Endpoints

### 1. Predict Burnout

```
POST /predict
```

**Input:** Prescription image
**Output:**

```json
{
  "prediction": "High",
  "confidence": 87.4,
  "probabilities": {
    "Low": 5.2,
    "Medium": 7.4,
    "High": 87.4
  }
}
```

---

### 2. Get All Records

```
GET /records
```

---

### 3. Download Excel Report

```
GET /download-excel
```

---

### 4. Send Email Report

```
POST /send-email
```

---

## 🛠️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/medpulse-ai.git
cd medpulse-ai
```

---

### 2. Setup Backend

```
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### 3. Run Frontend

```
cd frontend
python -m http.server 5500
```

Open:

```
http://localhost:5500
```

---

## 📊 Sample Workflow

1. Upload prescription image
2. System extracts handwriting features
3. ML model predicts burnout level
4. Data is stored
5. Admin can:

   * View dashboard
   * Download reports
   * Send reports via email

---

## 📈 Use Cases

* Hospital workforce monitoring
* Early burnout detection
* Mental health intervention planning
* Healthcare analytics systems
* AI-driven clinical decision support

---

## ⚠️ Limitations

* Requires trained model for high accuracy
* Browser demo uses simplified logic (if backend not connected)
* Email feature requires SMTP configuration

---

## 🔮 Future Enhancements

* Deep learning model (CNN-based)
* Real-time dashboard (WebSockets)
* Cloud deployment (AWS / Render)
* Authentication system (Admin login)
* Database integration (MongoDB)
* Explainable AI (SHAP / LIME)

---

## 👨‍💻 Contributors

* Swayam Singh
* Group 23 — AI & ML Department
* Symbiosis Institute of Technology, Pune

---

## 📜 License

This project is for academic and research purposes.

---

## ⭐ Acknowledgment

Special thanks to faculty guidance and real-world healthcare problem inspiration that motivated the development of this system.

---

## 💡 Tagline

> *“Detect burnout before it impacts lives.”*

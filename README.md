# **WhatsApp ML Prediction System (Twilio + Flask + Machine Learning)**

##  Project Overview
This project demonstrates a real-time machine learning system integrated with WhatsApp using Twilio and Flask. Users send comma-separated numerical values via WhatsApp, and the system predicts outcomes using a trained ML model and returns results instantly.

---

## How It Works

1. User sends numbers (comma-separated) via WhatsApp  
2. Twilio receives the message  
3. Flask server processes the request  
4. ML model predicts the result  
5. Response is sent back to WhatsApp instantly  

---

## Features

- WhatsApp integration using Twilio API  
- Real-time ML predictions  
- Flask-based backend server  
- Handles comma-separated numerical input  
- Fast and automated response system  

---

##  Tech Stack

- Python  
- Flask  
- Scikit-learn / Machine Learning Model  
- Twilio API  
- Ngrok (for local server exposure)

---
##  Structure
<img width="624" height="418" alt="image" src="https://github.com/user-attachments/assets/d6bb2219-7386-4265-93d0-3a10a56f5e7a" />

    ---


##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Whatsapp_ml_prediction_system.git
cd Whatsapp_ml_prediction_system

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Run Flask app

```bash
python app.py
```

### 4. Expose server using Ngrok

```bash
ngrok http 5000
```

### 5. Configure Twilio webhook
Paste your Ngrok URL in Twilio WhatsApp webhook settings
Set endpoint to /sms

## 📊 Project Flow Diagram

WhatsApp → Twilio → Flask API → ML Model → Response → WhatsApp

## 👨‍💻 Author

# Awais Manzoor

